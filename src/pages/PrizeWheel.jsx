import React, { useEffect, useRef, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import confetti from 'canvas-confetti';
import { supabase } from '../lib/supabase';
import './PrizeWheel.scss';

const SlotMachineReels = ({ couponList }) => {
  const source = couponList.length > 0 ? couponList : [
    'SUM-GR-0001', 'SUM-GR-0002', 'SUM-GR-0003', 'SUM-GR-0004', 'SUM-GR-0005', 'SUM-GR-0006'
  ];
  
  const generateStrip = () => {
    let rawCodes = [...source].sort(() => Math.random() - 0.5);
    while(rawCodes.length < 20) { rawCodes = [...rawCodes, ...rawCodes]; }
    const codes = rawCodes.slice(0, 20);
    return [...codes, ...codes, ...codes, ...codes, ...codes];
  };

  const strip1 = generateStrip();
  const strip2 = generateStrip();

  return (
    <div className="reels-wrap">
      <div className="reel-col reel-infinite-down">
        {strip1.map((v, i) => <div key={`c1-${i}`}>{v}</div>)}
      </div>
      <div className="reel-col reel-infinite-up">
        {strip2.map((v, i) => <div key={`c2-${i}`}>{v}</div>)}
      </div>
    </div>
  );
};

const PRIZES = {
  0: { img: '/assets/screen_wise_prizes/harley_podium.png', pureImg: '/assets/prizes/Harley Davidson.png', rank: 'GRAND PRIZE', tier: 'grand_prize', pageSize: 1, icon: '🏆' },
  1: { img: '/assets/screen_wise_prizes/bullet_podium.png', pureImg: '/assets/prizes/Bullet 1.png', rank: 'MEGA PRIZE', tier: 'mega_prize', pageSize: 1, icon: '🏍️' },
  2: { img: '/assets/screen_wise_prizes/cash_counting_podium.png', pureImg: '/assets/prizes/cash counting machine.png', rank: '3RD PRIZE', tier: '3rd_prize', pageSize: 10, icon: '💵' },
  3: { img: '/assets/screen_wise_prizes/godrej_safe_podium.png', pureImg: '/assets/prizes/godrej safe.png', rank: '4TH PRIZE', tier: '4th_prize', pageSize: 10, icon: '🔒' },
  4: { img: '/assets/screen_wise_prizes/chair_cushion.png', pureImg: '/assets/prizes/orthopedic chair cusion.png', rank: '5TH PRIZE', tier: '5th_prize', pageSize: 10, icon: '🪑' }
};

const PrizeWheel = () => {
  const { id } = useParams();
  const prize = PRIZES[parseInt(id)] || PRIZES[1];
  
  const canvasRef = useRef(null);
  const [mode, setMode] = useState('card'); // 'card', 'spin', 'reveal'
  const [wheelAngle, setWheelAngle] = useState(0);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [allWinners, setAllWinners] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [isSpinning, setIsSpinning] = useState(false);
  const [couponList, setCouponList] = useState([]);
  const [leftCode, setLeftCode] = useState('READY?');
  const [rightCode, setRightCode] = useState('SPIN NOW!');

  useEffect(() => {
    async function fetchCodes() {
      const { data } = await supabase.from('master_customers').select('coupon_code').neq('coupon_code', '').limit(150);
      if (data && data.length > 0) {
        const codes = data.map(r => r.coupon_code).filter(Boolean);
        if (codes.length > 0) setCouponList(codes);
      }
    }
    fetchCodes();
  }, []);


  // Constants for wheel
  const NS = 12; 
  const ARC = (Math.PI * 2) / NS;
  const SEGS = Array.from({length:NS},(_,i)=>{
    const c = i % 2 === 0 ? '#CBA135' : '#0B132C';
    return {color:c, light: c === '#CBA135' ? '#FDE68A' : '#1E293B'};
  });

  const max0 = (val) => Math.max(0, val);

  const drawWheel = (angle) => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const S = canvas.width;
    const cx = S / 2;
    const cy = S / 2;
    const R = S / 2 - 14;
    const ARC = (Math.PI * 2) / NS;
    ctx.clearRect(0, 0, S, S);

    /* Outer Gold Border (Metallic) */
    ctx.save(); ctx.shadowColor = "rgba(0,0,0,0.8)"; ctx.shadowBlur = 15;
    ctx.beginPath(); ctx.arc(cx, cy, R + 12, 0, Math.PI * 2);
    const oRim = ctx.createLinearGradient(0, 0, S, S);
    oRim.addColorStop(0, "#E2C275"); oRim.addColorStop(0.3, "#916B22"); oRim.addColorStop(0.5, "#FDF2C8"); oRim.addColorStop(0.7, "#654712"); oRim.addColorStop(1, "#D4AF37");
    ctx.fillStyle = oRim; ctx.fill(); ctx.restore();

    /* Dark Inner Rim Body */
    ctx.save();
    ctx.beginPath(); ctx.arc(cx, cy, R + 8, 0, Math.PI * 2);
    ctx.fillStyle = "#0B132C"; ctx.fill();
    ctx.restore();

    /* Rim dots */
    for(let d = 0; d < 24; d++){
      const da = angle + (d / 24) * Math.PI * 2;
      const dx = cx + Math.cos(da) * (R + 4), dy = cy + Math.sin(da) * (R + 4);
      ctx.save(); ctx.shadowColor = "rgba(255,235,150,0.8)"; ctx.shadowBlur = 10;
      ctx.beginPath(); ctx.arc(dx, dy, 2, 0, Math.PI * 2);
      ctx.fillStyle = "#FDF2C8"; ctx.fill(); ctx.restore();
    }

    /* Inner gold ring (Metallic) */
    ctx.save(); ctx.beginPath(); ctx.arc(cx, cy, R, 0, Math.PI * 2); 
    const iRim = ctx.createLinearGradient(0, S, S, 0);
    iRim.addColorStop(0, "#FDF2C8"); iRim.addColorStop(0.5, "#916B22"); iRim.addColorStop(1, "#E2C275");
    ctx.strokeStyle = iRim; ctx.lineWidth = 3; ctx.stroke(); ctx.restore();

    /* Segments */
    for(let i = 0; i < NS; i++){
      const start = angle + i * ARC - Math.PI / 2;
      const end = start + ARC;
      ctx.save();
      
      const grd = ctx.createRadialGradient(cx, cy, 0, cx, cy, R);
      grd.addColorStop(0, SEGS[i].light);
      grd.addColorStop(.55, SEGS[i].color);
      
      // dark version
      const hex = SEGS[i].color;
      const n = parseInt(hex.slice(1),16);
      const a = 55;
      const darkColor = `rgb(${max0(((n>>16)&0xff)-a)},${max0(((n>>8)&0xff)-a)},${max0((n&0xff)-a)})`;
      grd.addColorStop(1, darkColor);

      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.arc(cx, cy, R, start, end); ctx.closePath();
      ctx.fillStyle = grd; ctx.fill();
      
      // Subtle Texture
      ctx.clip(); 
      for(let s = 0; s < 15; s++){
        const rDist = (Math.sin(i * 20 + s * 45) * 0.5 + 0.5) * R;
        const rAng = start + (Math.cos(i * 30 + s * 15) * 0.5 + 0.5) * ARC;
        const stX = cx + Math.cos(rAng) * rDist;
        const stY = cy + Math.sin(rAng) * rDist;
        ctx.beginPath(); ctx.arc(stX, stY, Math.random() * 0.8, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(255,255,255," + (Math.random() * 0.2 + 0.05) + ")";
        ctx.fill();
      }
      
      // Fine Metallic Sheen
      const shGrd = ctx.createLinearGradient(cx + Math.cos(start) * R * .4, cy + Math.sin(start) * R * .4, cx + Math.cos(end) * R * .4, cy + Math.sin(end) * R * .4);
      shGrd.addColorStop(0, "rgba(255,255,255,.15)"); shGrd.addColorStop(.5, "transparent"); shGrd.addColorStop(1, "rgba(0,0,0,.15)");
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.arc(cx, cy, R, start, end); ctx.closePath(); ctx.fillStyle = shGrd; ctx.fill();
      ctx.restore();
      
      // Elegant Divider
      ctx.save();
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx + Math.cos(start) * R, cy + Math.sin(start) * R);
      ctx.strokeStyle = "rgba(255, 235, 150, 0.9)"; ctx.lineWidth = 1.5; ctx.stroke();
      ctx.strokeStyle = "rgba(0, 0, 0, 0.4)"; ctx.lineWidth = 0.5; ctx.stroke(); // subtle shadow edge
      ctx.restore();
    }
  };

  useEffect(() => {
    if (mode === 'spin') {
      drawWheel(wheelAngle);
    }
  }, [mode, wheelAngle]);

  const handleCardClick = () => {
    setMode('spin');
    document.body.classList.add('spin-mode');
  };

  const spinWheel = () => {
    if (isSpinning) return;
    setIsSpinning(true);
    setLeftCode('');
    setRightCode('');
    if (window.LuckyAudio) window.LuckyAudio.fanfare();
    const total = (Math.PI * 2) * (6 + Math.random() * 5);
    const dur = 4800, t0 = performance.now(), a0 = wheelAngle;
    let lastSeg = Math.floor(a0 / ARC);
    
    const ease = (t) => 1 - Math.pow(1 - t, 4);
    
    const frame = (now) => {
      const el = Math.min(now - t0, dur), t = el / dur;
      const newAngle = a0 + total * ease(t);
      setWheelAngle(newAngle);
      
      const seg = Math.floor(newAngle / ARC);
      if (seg !== lastSeg) {
        lastSeg = seg;
        if (window.LuckyAudio) window.LuckyAudio.tick();
      }
      
      if (el < dur) {
        requestAnimationFrame(frame);
      } else {
        onEnd();
      }
    };
    requestAnimationFrame(frame);
  };

  const onEnd = () => {
    setIsSpinning(false);
    setLeftCode('WINNERS');
    setRightCode('WINNERS');
    if (window.LuckyAudio) window.LuckyAudio.ding();
    
    const duration = 3000, end = Date.now() + duration;
    (function frame() {
      confetti({ particleCount: 5, angle: 60, spread: 55, origin: { x: 0 }, colors: ['#FFD700', '#00BCD4', '#FF4081'] });
      confetti({ particleCount: 5, angle: 120, spread: 55, origin: { x: 1 }, colors: ['#FFD700', '#00BCD4', '#FF4081'] });
      if (Date.now() < end) requestAnimationFrame(frame);
    }());

    setTimeout(() => {
      document.body.classList.remove('spin-mode');
      setMode('reveal');
    }, 2500);
  };

  const openModal = async () => {
    if (window.LuckyAudio) window.LuckyAudio.fanfare();
    try {
      const { data, error } = await supabase
        .from('draw_winners')
        .select('*')
        .eq('prize_tier', prize.tier);

      if (error) throw error;
      
      const winners = data.map(row => ({
        name: row.customer_name || '',
        mobile: row.coupon_code || '',
        district: row.territory || '',
        state: row.region || ''
      }));
      
      if (winners.length === 0) throw new Error("No winners");
      setAllWinners(winners);
    } catch (e) {
      console.error(e);
      // Demo Data Fallback
      setAllWinners(Array.from({length: Math.max(prize.pageSize*3, 12)}, (_, i) => ({
        name: `Demo Winner ${i+1}`,
        mobile: `1000${i}`,
        district: 'Demo Territory',
        state: 'Demo Region'
      })));
    }
    setCurrentPage(1);
    setIsModalOpen(true);
    if (window.LuckyAudio) { window.LuckyAudio.duck(true); setTimeout(() => window.LuckyAudio.celebrate(), 350); }
  };

  const closeModal = () => {
    setIsModalOpen(false);
    if (window.LuckyAudio) window.LuckyAudio.duck(false);
  };

  const totalPages = Math.ceil(allWinners.length / prize.pageSize) || 1;
  const start = (currentPage - 1) * prize.pageSize;
  const pageData = allWinners.slice(start, start + prize.pageSize);

  return (
    <div id="prize-page" className={mode === "spin" ? "spin-mode" : ""}>
      <Link to="/" className="home-btn">
        <svg viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>
        HOME
      </Link>

      <section className="hero">
        <div className="stage">
          <div className="dot-wall left"></div><div className="dot-wall right"></div>
          <div className="floor"></div>
          <div className="laser b1"><div className="halo"></div><div className="core"></div><div className="pulse"></div></div>
          <div className="laser b2"><div className="halo"></div><div className="core"></div><div className="pulse"></div></div>
          <div className="laser gold b3"><div className="halo"></div><div className="core"></div><div className="pulse"></div></div>
          <div className="laser gold b4"><div className="halo"></div><div className="core"></div><div className="pulse"></div></div>
          <div className="laser b5"><div className="halo"></div><div className="core"></div><div className="pulse"></div></div>
          <div className="laser b6"><div className="halo"></div><div className="core"></div><div className="pulse"></div></div>
          <div className="laser b7"><div className="halo"></div><div className="core"></div><div className="pulse"></div></div>
          <div className="emitter e1"></div><div className="emitter e2"></div><div className="emitter gold e3"></div><div className="emitter gold e4"></div><div className="emitter e5"></div><div className="emitter e6"></div><div className="emitter e7"></div>
          <div className="floor-glow"></div><div className="impact"></div>
          <div className="streak gold st1"></div><div className="streak blue st2"></div><div className="streak blue st3"></div><div className="streak gold st4"></div>
          <div className="particle white" style={{left: "12%", top: "18%", width: "4px", height: "4px"}}></div>
          <div className="particle blue" style={{left: "22%", top: "34%", width: "3px", height: "3px", animationDelay: ".8s"}}></div>
          <div className="particle gold" style={{left: "30%", top: "26%", width: "5px", height: "3px", animationDelay: "1.6s"}}></div>
          <div className="particle white" style={{left: "38%", top: "14%", width: "3px", height: "3px", animationDelay: ".4s"}}></div>
          <div className="particle blue" style={{left: "45%", top: "30%", width: "4px", height: "4px", animationDelay: "2s"}}></div>
          <div className="particle gold" style={{left: "58%", top: "22%", width: "5px", height: "3px", animationDelay: "1.1s"}}></div>
          <div className="particle white" style={{left: "66%", top: "12%", width: "3px", height: "3px", animationDelay: ".2s"}}></div>
          <div className="particle blue" style={{left: "74%", top: "28%", width: "4px", height: "4px", animationDelay: "1.8s"}}></div>
          <div className="particle gold" style={{left: "82%", top: "36%", width: "5px", height: "3px", animationDelay: ".6s"}}></div>
          <div className="particle white" style={{left: "88%", top: "20%", width: "4px", height: "4px", animationDelay: "2.4s"}}></div>
          <div className="particle blue" style={{left: "16%", top: "48%", width: "3px", height: "3px", animationDelay: "1.4s"}}></div>
          <div className="particle blue" style={{left: "84%", top: "50%", width: "3px", height: "3px", animationDelay: ".9s"}}></div>
          <div className="particle gold" style={{left: "55%", top: "42%", width: "4px", height: "3px", animationDelay: "2.2s"}}></div>
          <div className="particle white" style={{left: "50%", top: "8%", width: "3px", height: "3px", animationDelay: "1s"}}></div>
          <div className="vignette"></div>
        </div>

        <div className="content">
          <div className="header-logos">
            <video src="/assets/logo.webm" autoPlay loop muted playsInline className="logo-left" />
          </div>

          <div className="prize-img-wrap" style={{position: 'relative'}}>
            <img src="/assets/images/granulam_podium.png" alt="Granulam Left" className="prize-img-side side-left" />
            <img id="prize-img" src={prize.img} alt="Prize" className="prize-img" />
            <img src="/assets/images/granulam_podium.png" alt="Granulam Right" className="prize-img-side side-right" />
          </div>

          <div className="card-zone">
            <div className="spin-action-area" id="card-wrap" onClick={handleCardClick} style={{cursor:"pointer", display: mode === "card" ? "flex" : "none"}}>
              <div className="spin-text-top">SPIN THE WHEEL & WIN</div>
              <div className="spin-text-sub"><span className="line"></span> AMAZING PRIZES <span className="line"></span></div>
              <button className="spin-now-btn">SPIN NOW <span className="arrow">›</span></button>
            </div>

            <div id="wheel-zone" className={mode === "spin" ? "active" : ""} style={{ opacity: mode === "spin" ? 1 : 0, transition: "opacity 0.6s" }}>
              <div className="ticker-side ticker-left">
                <div className="ticker-code">
                  {isSpinning ? <SlotMachineReels couponList={couponList} /> : leftCode}
                </div>
              </div>

              <div className="wheel-outer-wrap">
                <div className="wheel-halo">
                  <div className="wheel-container" id="wheel-container">
                    <div className="wheel-pointer"></div>
                    <canvas id="wheel-canvas" ref={canvasRef} width="500" height="500"></canvas>
                    <div className="wheel-center-btn" id="spin-btn" onClick={spinWheel}>
                      <div className="spin-text">SPIN</div>
                      <div className="ampersand">&amp;</div>
                      <div className="win-text">WIN</div>
                    </div>
                  </div>
                  
                </div>
                <div className="wheel-label" id="wheel-label">{isSpinning ? "🎰 SPINNING..." : "✦ TAP THE WHEEL TO SPIN ✦"}</div>
              </div>

              <div className="ticker-side ticker-right">
                <div className="ticker-code">
                  {isSpinning ? <SlotMachineReels couponList={couponList} /> : rightCode}
                </div>
              </div>
            </div>
          </div>

        </div>
      </section>

      <div id="reveal-btn-wrap" className={mode === "reveal" ? "show" : ""}>
        <button id="reveal-btn" onClick={openModal}>🏆 &nbsp;REVEAL WINNERS!</button>
      </div>

      <div id="modal-overlay" className={isModalOpen ? "open" : ""} onClick={(e) => { if (e.target.id === "modal-overlay") closeModal(); }}>
        {isModalOpen && <img src={prize.img} alt="Prize Left" className="carousel-prize-side side-left" />}
        <div className="modal">
          <div className="modal-header">
            <div className="modal-title" id="modal-title" style={{display:"flex", alignItems:"center", gap:"8px"}}>
              <span dangerouslySetInnerHTML={{__html: prize.icon}} /> {prize.rank} — Winners
            </div>
            <button className="modal-close" onClick={closeModal}>✕</button>
          </div>
          <div className="modal-body" id="carousel-content">
            {prize.pageSize <= 2 ? (
              <div style={{display:"flex", gap:"20px", justifyContent:"center"}}>
                {pageData.map((w, idx) => (
                  <div className="winner-single" key={idx}>
                    <div className="winner-trophy">🏆</div>
                    <div className="winner-big-num">#{start + idx + 1}</div>
                    <div className="winner-card-single">
                      <div className="w-name">{w.name}</div>
                      <div className="w-loc">📍 {w.state}, {w.district}</div>
                      <div className="w-mobile">📱 {w.mobile}</div>
                    </div>
                  </div>
                ))}
              </div>
            ) : (
              <table className="winners-table">
                <thead><tr><th>#</th><th>Name</th><th>Region</th><th>Territory</th><th>Coupon code</th></tr></thead>
                <tbody>
                  {pageData.map((w, idx) => (
                    <tr key={idx} className={start+idx===0 && currentPage===1 ? "top-win" : ""}>
                      <td><div className="row-num">{start + idx + 1}</div></td>
                      <td><div className="td-name">{w.name}</div></td>
                      <td><div className="td-state">{w.state}</div></td>
                      <td><div className="td-district">{w.district}</div></td>
                      <td><div className="td-mobile">{w.mobile}</div></td>
                    </tr>
                  ))}
                </tbody>
              </table>
            )}
          </div>
          <div className="carousel-nav">
            <button className="nav-btn" id="prev-btn" disabled={currentPage === 1} onClick={() => {setCurrentPage(currentPage - 1); if(window.LuckyAudio) window.LuckyAudio.page();}}>← Prev</button>
            <div className="page-info-wrap">
              <span className="page-label" id="page-label">{prize.pageSize > 2 ? `Winners ${start+1}–${Math.min(start+prize.pageSize, allWinners.length)} of ${allWinners.length}` : "Winner"}</span>
              <span className="page-num" id="page-num">{currentPage}</span>
              <span className="page-of" id="page-of">of {totalPages}</span>
            </div>
            <button className="nav-btn" id="next-btn" disabled={currentPage >= totalPages} onClick={() => {setCurrentPage(currentPage + 1); if(window.LuckyAudio) window.LuckyAudio.page();}}>Next →</button>
          </div>
        </div>
        {isModalOpen && <img src={prize.img} alt="Prize Right" className="carousel-prize-side side-right" />}
      </div>
    </div>
  );
}

export default PrizeWheel;
