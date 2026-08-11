/* ═══════════════════════════════════════════════════════════════
   LUCKY DRAW AUDIO ENGINE  (shared by index.html & prize.html)
   ─ Background music: loops from assets/audio/bg_music.mp3 in the GitHub repo,
     resumes position across page changes, fades in/out smoothly.
   ─ If assets/audio/bg_music.mp3 is missing, falls back to a built-in festive
     synth loop so the event is never silent.
   ─ Sound FX (wheel ticks, ding, fanfare, celebration) are
     synthesized in-browser: no files, no lag, no copyright risk.
   ─ Bottom-right widget: play/pause + volume slider (remembered).
   ═══════════════════════════════════════════════════════════════ */
window.LuckyAudio = (function () {
  'use strict';

  /* ── CONFIG ── */
  /* The site tries these locations in order until one loads. */
  var BGM_CANDIDATES = [
    'assets/audio/bg_music.mp3'
  ];
  var BGM_MAX = 0.45;            // background bed stays quiet under your voice
  var DUCK    = 0.30;            // music drops to 30% while winners are shown
  var FADE_IN = 1400;            // ms

  /* ── PERSISTED STATE ── */
  var vol     = clamp(parseFloat(localStorage.getItem('ld_vol')), 0, 1);
  if (isNaN(vol)) vol = 0.6;
  var paused  = localStorage.getItem('ld_paused') === '1';
  var resumeT = parseFloat(sessionStorage.getItem('ld_time')) || 0;

  var ducked = false, started = false, usingFallback = false;

  function clamp(n, a, b) { return Math.min(b, Math.max(a, n)); }

  /* ══════════════ WEB AUDIO (sound FX + fallback music) ══════════════ */
  var ctx = null, sfxGain = null;
  function audioCtx() {
    if (!ctx) {
      var AC = window.AudioContext || window.webkitAudioContext;
      if (!AC) return null;
      ctx = new AC();
      sfxGain = ctx.createGain();
      sfxGain.gain.value = vol;
      sfxGain.connect(ctx.destination);
      if (typeof decodeApplause === 'function') decodeApplause();
    }
    if (ctx.state === 'suspended') ctx.resume();
    return ctx;
  }

  /* ── BACKGROUND MUSIC ELEMENT ── */
  var bgm = new Audio();
  bgm.loop = true;
  bgm.preload = 'auto';
  bgm.volume = 0;

  var bgmIdx = 0;
  function loadNextBgm() {
    if (bgmIdx >= BGM_CANDIDATES.length) {
      console.warn('[LuckyAudio] No background music file found. ' +
        'Put your track named exactly "assets/audio/bg_music.mp3" in the SAME folder as index.html. ' +
        'Tried: ' + BGM_CANDIDATES.join(', ') + '. Using built-in fallback music for now.');
      useFallbackMusic();
      return;
    }
    bgm.src = BGM_CANDIDATES[bgmIdx++];
    bgm.load();
  }
  bgm.addEventListener('error', loadNextBgm);
  bgm.addEventListener('canplaythrough', function () {
    console.log('[LuckyAudio] Background music loaded: ' + bgm.src.split('/').pop());
    if (unlocked && !paused && bgm.paused) startMusic();
  }, { once: true });
  loadNextBgm();

  /* Smooth volume targeting (one rAF loop handles fades + ducking) */
  var fadeStart = 0, fadeFrom = 0, fading = false;
  function targetVol() { return paused ? 0 : vol * BGM_MAX * (ducked ? DUCK : 1); }
  function fadeTo(ms) {
    fadeStart = performance.now(); fadeFrom = currentMusicVol(); fading = true; fadeMs = ms || 600;
  }
  var fadeMs = 600;
  function currentMusicVol() { return usingFallback ? fbGainVal : bgm.volume; }
  function setMusicVol(v) {
    v = clamp(v, 0, 1);
    if (usingFallback) { if (fbGain) fbGain.gain.value = v; fbGainVal = v; }
    else bgm.volume = v;
  }
  (function fadeLoop(now) {
    if (fading) {
      var t = clamp((now - fadeStart) / fadeMs, 0, 1);
      setMusicVol(fadeFrom + (targetVol() - fadeFrom) * t);
      if (t >= 1) fading = false;
    }
    requestAnimationFrame(fadeLoop);
  })(0);

  /* ── START / RESUME ── */
  var unlocked = false;
  function startMusic() {
    if (paused) return;
    if (usingFallback) {
      if (unlocked) { startFallback(); started = true; fadeTo(FADE_IN); updateBtn(); }
      return;
    }
    if (started && !bgm.paused) return;
    try { if (resumeT > 1 && (!isFinite(bgm.duration) || resumeT < bgm.duration)) bgm.currentTime = resumeT; } catch (e) {}
    var p = bgm.play();
    if (p && p.then) {
      p.then(function () { started = true; fadeTo(FADE_IN); updateBtn(); })
       .catch(function () { /* autoplay blocked or src still loading – retried on next click / canplaythrough */ });
    }
  }

  /* Try immediately (works if browser allows), else on first interaction */
  function unlock() { unlocked = true; audioCtx(); startMusic(); }
  document.addEventListener('pointerdown', unlock, { capture: true });
  document.addEventListener('keydown', unlock, { capture: true });
  startMusic();

  /* Save playback position so the next page resumes seamlessly */
  setInterval(function () {
    if (!usingFallback && started && !bgm.paused) sessionStorage.setItem('ld_time', bgm.currentTime.toFixed(2));
  }, 1000);
  window.addEventListener('pagehide', function () {
    if (!usingFallback && started) sessionStorage.setItem('ld_time', bgm.currentTime.toFixed(2));
  });

  /* ── FALLBACK FESTIVE LOOP (only if assets/audio/bg_music.mp3 is unavailable) ── */
  var fbGain = null, fbTimer = null, fbGainVal = 0;
  function useFallbackMusic() {
    usingFallback = true;
    if (unlocked && !paused) { startFallback(); started = true; fadeTo(FADE_IN); updateBtn(); }
  }
  function startFallback() {
    var c = audioCtx(); if (!c || fbTimer) return;
    fbGain = c.createGain(); fbGain.gain.value = 0; fbGainVal = 0;
    fbGain.connect(c.destination);
    var notes = [261.63, 329.63, 392.0, 523.25, 392.0, 329.63];  // C-E-G arpeggio
    var bass  = [130.81, 130.81, 174.61, 196.0];
    var step = 0;
    fbTimer = setInterval(function () {
      if (paused) return;
      var t = c.currentTime;
      tone(c, fbGain, notes[step % notes.length], t, 0.5, 'triangle', 0.5);
      if (step % 3 === 0) tone(c, fbGain, bass[(step / 3 | 0) % bass.length], t, 1.0, 'sine', 0.7);
      step++;
    }, 340);
  }
  function tone(c, dest, freq, t, dur, type, g) {
    var o = c.createOscillator(), gn = c.createGain();
    o.type = type; o.frequency.value = freq;
    gn.gain.setValueAtTime(0.0001, t);
    gn.gain.exponentialRampToValueAtTime(g, t + 0.03);
    gn.gain.exponentialRampToValueAtTime(0.0001, t + dur);
    o.connect(gn); gn.connect(dest);
    o.start(t); o.stop(t + dur + 0.05);
  }

  /* ══════════════ SOUND EFFECTS (all synthesized) ══════════════ */
  function sfxTone(freq, dur, type, gain, when, slideTo) {
    var c = audioCtx(); if (!c || vol <= 0) return;
    var t = c.currentTime + (when || 0);
    var o = c.createOscillator(), g = c.createGain();
    o.type = type || 'sine'; o.frequency.setValueAtTime(freq, t);
    if (slideTo) o.frequency.exponentialRampToValueAtTime(slideTo, t + dur);
    g.gain.setValueAtTime(0.0001, t);
    g.gain.exponentialRampToValueAtTime(gain || 0.5, t + 0.012);
    g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
    o.connect(g); g.connect(sfxGain);
    o.start(t); o.stop(t + dur + 0.05);
  }
  function noiseBurst(dur, gain, fStart, fEnd, when) {
    var c = audioCtx(); if (!c || vol <= 0) return;
    var t = c.currentTime + (when || 0);
    var len = Math.max(1, c.sampleRate * dur) | 0;
    var buf = c.createBuffer(1, len, c.sampleRate);
    var d = buf.getChannelData(0);
    for (var i = 0; i < len; i++) d[i] = Math.random() * 2 - 1;
    var src = c.createBufferSource(); src.buffer = buf;
    var f = c.createBiquadFilter(); f.type = 'bandpass'; f.Q.value = 0.9;
    f.frequency.setValueAtTime(fStart, t);
    f.frequency.exponentialRampToValueAtTime(fEnd, t + dur);
    var g = c.createGain();
    g.gain.setValueAtTime(gain, t);
    g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
    src.connect(f); f.connect(g); g.connect(sfxGain);
    src.start(t); src.stop(t + dur + 0.05);
  }

  /* ══ APPLAUSE: real recording (assets/audio/applause.mp3) with synth fallback ══ */
  var APPLAUSE_CANDIDATES = [
    'assets/audio/applause.mp3'
  ];
  var applauseFileBuf = null, applauseRaw = null;
  (function fetchApplause(i) {
    if (i >= APPLAUSE_CANDIDATES.length) {
      console.warn('[LuckyAudio] assets/audio/applause.mp3 not found next to the website — using synthetic claps. ' +
        'Upload assets/audio/applause.mp3 to the same folder as index.html for real claps.');
      return;
    }
    fetch(APPLAUSE_CANDIDATES[i])
      .then(function (r) { if (!r.ok) throw 0; return r.arrayBuffer(); })
      .then(function (ab) { applauseRaw = ab; if (ctx) decodeApplause(); })
      .catch(function () { fetchApplause(i + 1); });
  })(0);
  function decodeApplause() {
    if (!applauseRaw || applauseFileBuf) return;
    ctx.decodeAudioData(applauseRaw.slice(0), function (b) {
      applauseFileBuf = b;
      console.log('[LuckyAudio] Real applause recording loaded.');
    }, function () {});
  }

  /* Synthetic fallback: dozens of tiny clap bursts rendered into one buffer */
  var applauseBuf = null;
  function buildApplause(c) {
    var dur = 3.2, sr = c.sampleRate, len = (sr * dur) | 0;
    var buf = c.createBuffer(1, len, sr), d = buf.getChannelData(0);
    var claps = 170;
    for (var k = 0; k < claps; k++) {
      /* denser at the start, thinning toward the end */
      var start = Math.pow(Math.random(), 1.6) * (dur - 0.15);
      var s0 = (start * sr) | 0;
      var cl = (sr * (0.012 + Math.random() * 0.018)) | 0;   // each clap 12–30ms
      var amp = 0.25 + Math.random() * 0.5;
      for (var i = 0; i < cl && s0 + i < len; i++) {
        var env = Math.exp(-i / (cl * 0.28));
        d[s0 + i] += (Math.random() * 2 - 1) * amp * env;
      }
    }
    /* gentle overall fade-out */
    var fadeS = (sr * 0.9) | 0;
    for (var j = 0; j < fadeS; j++) d[len - 1 - j] *= j / fadeS;
    return buf;
  }
  function playApplause(level) {
    var c = audioCtx(); if (!c || vol <= 0) return;
    var g = c.createGain();
    if (applauseFileBuf) {
      /* real recording */
      var src = c.createBufferSource(); src.buffer = applauseFileBuf;
      g.gain.value = (level || 0.55) * 1.5;
      src.connect(g); g.connect(sfxGain);
      src.start();
      return;
    }
    /* synthetic fallback */
    if (!applauseBuf) applauseBuf = buildApplause(c);
    var s2 = c.createBufferSource(); s2.buffer = applauseBuf;
    var f = c.createBiquadFilter(); f.type = 'bandpass'; f.frequency.value = 1500; f.Q.value = 0.5;
    g.gain.value = level || 0.55;
    s2.connect(f); f.connect(g); g.connect(sfxGain);
    s2.start();
  }

  var api = {
    /* wheel passes a segment boundary → mechanical "tick" */
    tick: function () {
      sfxTone(1900, 0.035, 'square', 0.16);
      noiseBurst(0.025, 0.10, 4000, 2500);
    },
    /* wheel lands → bright bell ding */
    ding: function () {
      sfxTone(1318.5, 0.9, 'sine', 0.45);
      sfxTone(2637.0, 0.6, 'sine', 0.18);
      sfxTone(1979.5, 0.45, 'sine', 0.12, 0.04);
    },
    /* card → wheel transition */
    whoosh: function () { noiseBurst(0.45, 0.30, 300, 3200); },
    /* REVEAL button → rising fanfare */
    fanfare: function () {
      var n = [523.25, 659.25, 783.99, 1046.5];
      for (var i = 0; i < n.length; i++) {
        sfxTone(n[i], 0.42, 'sawtooth', 0.16, i * 0.13);
        sfxTone(n[i] / 2, 0.42, 'triangle', 0.14, i * 0.13);
      }
      sfxTone(1046.5, 0.9, 'triangle', 0.22, 0.52);
    },
    /* winners carousel opens → claps + celebration shimmer */
    applause: function () { playApplause(); },
    celebrate: function () {
      playApplause();
      var chord = [523.25, 659.25, 783.99, 1046.5, 1318.5];
      for (var i = 0; i < chord.length; i++) sfxTone(chord[i], 1.1, 'triangle', 0.12, 0.02 * i);
      for (var j = 0; j < 7; j++) sfxTone(1400 + Math.random() * 1800, 0.22, 'sine', 0.10, 0.1 + j * 0.085);
    },
    /* carousel page change → soft flip + light claps for the new winner(s) */
    page: function () {
      sfxTone(880, 0.06, 'triangle', 0.14);
      playApplause(0.32);
    },
    /* lower / restore music under the winners modal */
    duck: function (on) { ducked = !!on; fadeTo(500); }
  };

  /* ══════════════ CONTROL WIDGET (bottom-right) ══════════════ */
  var css = document.createElement('style');
  css.textContent =
    '#ld-audio-ctl{position:fixed;right:20px;bottom:20px;z-index:900;display:flex;flex-direction:column;align-items:center;gap:10px;' +
      'padding:14px 10px;border-radius:40px;' +
      'background:linear-gradient(160deg,rgba(34,40,86,.88),rgba(17,24,56,.94));' +
      'border:1.5px solid rgba(255,215,0,.45);backdrop-filter:blur(14px);' +
      'box-shadow:0 6px 24px rgba(0,0,0,.6),0 0 18px rgba(255,215,0,.18),inset 0 1px 0 rgba(255,255,255,.15);}' +
    '#ld-play{width:36px;height:36px;border-radius:50%;border:none;cursor:pointer;flex-shrink:0;' +
      'background:linear-gradient(135deg,#FFD700,#FFF4CC);display:flex;align-items:center;justify-content:center;' +
      'box-shadow:0 3px 12px rgba(255,215,0,.5);transition:transform .2s,box-shadow .2s;}' +
    '#ld-play:hover{transform:scale(1.1);box-shadow:0 4px 18px rgba(255,215,0,.8);}' +
    '#ld-play svg{width:16px;height:16px;fill:#020A1A;}' +
    '#ld-vol-wrap{position:relative;width:20px;height:90px;display:flex;justify-content:center;align-items:center;}' +
    '#ld-vol{-webkit-appearance:none;appearance:none;width:80px;height:6px;border-radius:4px;outline:none;cursor:pointer;' +
      'background:linear-gradient(90deg,#FFD700 var(--p,60%),rgba(255,215,0,.2) var(--p,60%));' +
      'transform:rotate(-90deg);position:absolute;}' +
    '#ld-vol::-webkit-slider-thumb{-webkit-appearance:none;width:15px;height:15px;border-radius:50%;' +
      'background:radial-gradient(circle at 35% 35%,#FFF3C0,#FFD700 45%,#B8860B);' +
      'box-shadow:0 0 8px rgba(255,210,0,.8);cursor:pointer;}' +
    '#ld-vol::-moz-range-thumb{width:15px;height:15px;border:none;border-radius:50%;' +
      'background:radial-gradient(circle at 35% 35%,#FFF3C0,#FFD700 45%,#B8860B);box-shadow:0 0 8px rgba(255,210,0,.8);cursor:pointer;}' +
    '#ld-audio-ctl .ld-ico{display:flex;align-items:center;justify-content:center;width:18px;height:18px;}' +
    '#ld-audio-ctl .ld-ico svg{width:18px;height:18px;fill:rgba(255,215,0,0.9);filter:drop-shadow(0 0 4px rgba(255,215,0,0.5));}' +
    '@media (max-width:560px){#ld-audio-ctl{right:8px;bottom:8px;padding:12px 8px;}#ld-vol-wrap{height:70px;}#ld-vol{width:60px;}}';
  document.head.appendChild(css);

  var SVG_PLAY  = '<svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>';
  var SVG_PAUSE = '<svg viewBox="0 0 24 24"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>';
  var SVG_VOL_DOWN = '<svg viewBox="0 0 24 24"><path d="M18.5 12c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM5 9v6h4l5 5V4L9 9H5z"/></svg>';
  var SVG_VOL_UP = '<svg viewBox="0 0 24 24"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg>';

  var wrap = document.createElement('div');
  wrap.id = 'ld-audio-ctl';
  wrap.innerHTML =
    '<button id="ld-play" title="Play / pause music"></button>' +
    '<div class="ld-ico" title="Volume Up" style="margin-top:4px;">' + SVG_VOL_UP + '</div>' +
    '<div id="ld-vol-wrap"><input id="ld-vol" type="range" min="0" max="100" step="1" title="Volume"></div>' +
    '<div class="ld-ico" title="Volume Down" style="margin-bottom:4px;">' + SVG_VOL_DOWN + '</div>';
  function mount() { document.body.appendChild(wrap); init(); }
  if (document.body) mount(); else document.addEventListener('DOMContentLoaded', mount);

  var btn, slider;
  function init() {
    btn = document.getElementById('ld-play');
    slider = document.getElementById('ld-vol');
    slider.value = Math.round(vol * 100);
    slider.style.setProperty('--p', slider.value + '%');
    updateBtn();

    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      paused = !paused;
      localStorage.setItem('ld_paused', paused ? '1' : '0');
      if (!paused) { unlock(); if (!usingFallback && bgm.paused) bgm.play().catch(function(){}); }
      fadeTo(450);
      if (paused) setTimeout(function () { if (!usingFallback && paused) bgm.pause(); }, 500);
      updateBtn();
    });

    slider.addEventListener('input', function () {
      vol = slider.value / 100;
      localStorage.setItem('ld_vol', vol);
      slider.style.setProperty('--p', slider.value + '%');
      if (sfxGain) sfxGain.gain.value = vol;
      fadeTo(120);
    });
  }
  function updateBtn() { if (btn) btn.innerHTML = paused ? SVG_PLAY : SVG_PAUSE; }

  return api;
})();
