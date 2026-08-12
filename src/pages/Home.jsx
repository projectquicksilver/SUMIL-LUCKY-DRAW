import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';
import './Home.scss';

const Home = () => {
  useEffect(() => {
    // Generate particle effects on mount (from the vanilla script)
    const layer = document.getElementById('fx');
    if (!layer) return;
    
    // Clear existing to avoid duplicates on re-render
    layer.innerHTML = '';
    
    const colors = ['#D4A017','#FFD966','#FF6B00','#FF3B3B','#FFF5DC','#B87333','#FF9060'];
    for (let i = 0; i < 65; i++) {
      const el = document.createElement('div'); el.className = 'cf';
      const c = colors[i % colors.length], w = 4 + Math.random()*10, h = w*(Math.random()>.4?2.5:1);
      el.style.cssText = `left:${Math.random()*100}%;width:${w}px;height:${h}px;background:${c};border-radius:${Math.random()>.5?'50%':'3px'};animation-delay:${Math.random()*12}s;animation-duration:${7+Math.random()*9}s;`;
      layer.appendChild(el);
    }
    for (let i = 0; i < 24; i++) {
      const s = document.createElement('div'); s.className = 'sp';
      const sz = 3 + Math.random()*10;
      s.style.cssText = `left:${Math.random()*100}%;top:${Math.random()*95}%;width:${sz}px;height:${sz}px;animation-delay:${Math.random()*4}s;animation-duration:${1.5+Math.random()*3}s;`;
      layer.appendChild(s);
    }
    for (let i = 0; i < 7; i++) {
      const o = document.createElement('div'); o.className = 'orb';
      const sz = 60 + Math.random()*180;
      o.style.cssText = `left:${Math.random()*100}%;top:${Math.random()*100}%;width:${sz}px;height:${sz}px;animation-delay:${Math.random()*5}s;animation-duration:${5+Math.random()*6}s;`;
      layer.appendChild(o);
    }
  }, []);

  return (
    <div id="home-page">
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

    {/*  TOP GROUP: logos + banner + strip + main image + divider  */}
    <div className="top-group">

    {/*  HEADER LOGOS  */}
    <div className="header-logos">
      <div className="logo-left-wrap" style={{position: "relative", zIndex: "10"}}>
        <video src="assets/logo.webm" autoPlay loop muted playsInline className="logo-left" />
      </div>
    </div>

    {/*  BANNER CONTAINER  */}
    <div style={{position: "relative", width: "100%", display: "flex", justifyContent: "center", alignItems: "center", marginTop: "5px"}}>
      
      {/*  SPINNING WHEEL (LEFT)  */}
      <div className="podium-wrapper" style={{right: "auto", left: "-2%", height: "42vh", width: "35vw"}}>
        {/*  Falling celebration particles over the wheel  */}
        <div className="falling-star" style={{left: "20%", animationDelay: "0.2s", background: "#FF3B3B"}}></div>
        <div className="falling-star" style={{left: "50%", animationDelay: "0.9s", background: "#FFD700"}}></div>
        <div className="falling-star" style={{left: "80%", animationDelay: "1.6s", background: "#4caf50"}}></div>
        <div className="falling-star" style={{left: "35%", animationDelay: "0.5s", background: "#FF9060"}}></div>
        <div className="falling-star" style={{left: "65%", animationDelay: "1.2s", background: "#FFD966"}}></div>
        
        <img src="assets/images/Spin_this_wheel.gif" alt="Spinning Wheel" style={{height: "100%", width: "100%", objectFit: "contain", animation: "granulamCelebrate 4s infinite ease-in-out"}}/>
      </div>

      {/*  TITLE BANNER  */}
      <img src="assets/images/main_banner.png" alt="Main Banner" className="title-banner" style={{height: "48vh", width: "100%", maxWidth: "1200px", objectFit: "contain", zIndex: "2"}}/>
      
      {/*  GRANULAM PODIUM  */}
      <div className="podium-wrapper" style={{right: "5%", top: "55%", height: "28vh", width: "25vw"}}>
        {/*  Falling celebration particles over the podium  */}
        <div className="falling-star" style={{left: "20%", animationDelay: "0.1s", background: "#FF3B3B"}}></div>
        <div className="falling-star" style={{left: "50%", animationDelay: "0.8s", background: "#FFD700"}}></div>
        <div className="falling-star" style={{left: "80%", animationDelay: "1.5s", background: "#4caf50"}}></div>
        <div className="falling-star" style={{left: "35%", animationDelay: "0.4s", background: "#FF9060"}}></div>
        <div className="falling-star" style={{left: "65%", animationDelay: "1.1s", background: "#FFD966"}}></div>
        
        <img src="assets/images/granulam_podium.png" alt="Granulam Podium" style={{height: "100%", width: "100%", objectFit: "contain", animation: "granulamCelebrate 4s infinite ease-in-out"}}/>
      </div>
      
    </div>



    </div>{/*  end .top-group  */}

{/*  PRIZE CARDS ROW — no badge images, animated word-art ranks  */}
    <div className="cards-row">

      {/*  GRAND PRIZE  */}
      <Link className="pcard-wrap grand-card" to="/prize/0">
        <div className="pcard">
          <div className="pcard-spotlight"></div>
          <div className="pcard-body">
            <div className="pcard-platform">
              <div className="ring3"></div><div className="pcard-platform-inner"></div>
              <img src="assets/screen_wise_prizes/harley_podium.png"
                   alt="Harley Davidson" className="pcard-img" style={{animationDelay: "0s"}}/>
            </div>
            <div className="pcard-rank-art" style={{display: "flex", alignItems: "center", justifyContent: "center", gap: "6px"}}><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/><path d="M4 22h16"/><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"/><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"/><path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"/></svg> GRAND PRIZE</div>
            <div className="pcard-name">HARLEY-DAVIDSON<br/>X440 BIKE</div>
            <div className="pcard-sub">Harley-Davidson X440</div>
            <span className="pcard-qty">🎁 × 1 Winner</span>
            <div className="pcard-hint">🎯 View &amp; Spin</div>
          </div>
        </div>
      </Link>

      {/*  MEGA PRIZE  */}
      <Link className="pcard-wrap mega-card" to="/prize/1">
        <div className="pcard">
          <div className="pcard-spotlight"></div>
          <div className="pcard-body">
            <div className="pcard-platform">
              <div className="ring3"></div><div className="pcard-platform-inner"></div>
              <img src="assets/screen_wise_prizes/bullet_podium.png"
                   alt="Royal Enfield Bike" className="pcard-img" style={{animationDelay: "0.5s"}}/>
            </div>
            <div className="pcard-rank-art" style={{display: "flex", alignItems: "center", justifyContent: "center", gap: "6px"}}><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m2 4 3 12h14l3-12-6 7-4-7-4 7-6-7zm3 16h14"/></svg> MEGA PRIZE</div>
            <div className="pcard-name">ROYAL ENFIELD<br/>BIKES</div>
            <div className="pcard-sub">Royal Enfield Bike</div>
            <span className="pcard-qty">🎁 × 2 Winners</span>
            <div className="pcard-hint">🎯 View &amp; Spin</div>
          </div>
        </div>
      </Link>

      {/*  2ND PRIZE (3RD PRIZE)  */}
      <Link className="pcard-wrap ranka-card" to="/prize/2">
        <div className="pcard">
          <div className="pcard-spotlight"></div>
          <div className="pcard-body">
            <div className="pcard-platform">
              <div className="ring3"></div><div className="pcard-platform-inner"></div>
              <img src="assets/screen_wise_prizes/cash_counting_podium.png"
                   alt="Cash Counting Machine" className="pcard-img" style={{animationDelay: "0.2s"}}/>
            </div>
            <div className="pcard-rank-art" style={{display: "flex", alignItems: "center", justifyContent: "center", gap: "6px"}}><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M7.21 15 2.66 7.14a2 2 0 0 1 .13-2.2L4.4 2.8A2 2 0 0 1 6 2h12a2 2 0 0 1 1.6.8l1.6 2.14a2 2 0 0 1 .14 2.2L16.79 15"/><path d="M11 12 5.12 2.2"/><path d="m13 12 5.88-9.8"/><path d="M8 7h8"/><circle cx="12" cy="17" r="5"/><path d="M12 18v-2h-.5"/></svg> 3RD PRIZE</div>
            <div className="pcard-name">CASH COUNTING<br/>MACHINE</div>
            <div className="pcard-sub">Heavy Duty</div>
            <span className="pcard-qty">🎁 × 50 Winners</span>
            <div className="pcard-hint">🎯 View &amp; Spin</div>
          </div>
        </div>
      </Link>

      {/*  3RD PRIZE (4TH PRIZE)  */}
      <Link className="pcard-wrap rankb-card" to="/prize/3">
        <div className="pcard">
          <div className="pcard-spotlight"></div>
          <div className="pcard-body">
            <div className="pcard-platform">
              <div className="ring3"></div><div className="pcard-platform-inner"></div>
              <img src="assets/screen_wise_prizes/godrej_safe_podium.png"
                   alt="Godrej Safe" className="pcard-img" style={{animationDelay: "0.7s"}}/>
            </div>
            <div className="pcard-rank-art" style={{display: "flex", alignItems: "center", justifyContent: "center", gap: "6px"}}><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/></svg> 4TH PRIZE</div>
            <div className="pcard-name">GODREJ<br/>SAFE</div>
            <div className="pcard-sub">Digital Locker</div>
            <span className="pcard-qty">🎁 × 100 Winners</span>
            <div className="pcard-hint">🎯 View &amp; Spin</div>
          </div>
        </div>
      </Link>

      {/*  4TH PRIZE (5TH PRIZE)  */}
      <Link className="pcard-wrap rankc-card" to="/prize/4">
        <div className="pcard">
          <div className="pcard-spotlight"></div>
          <div className="pcard-body">
            <div className="pcard-platform">
              <div className="ring3"></div><div className="pcard-platform-inner"></div>
              <img src="assets/screen_wise_prizes/chair_cushion.png"
                   alt="Orthopedic Chair" className="pcard-img" style={{animationDelay: "0.4s"}}/>
            </div>
            <div className="pcard-rank-art" style={{display: "flex", alignItems: "center", justifyContent: "center", gap: "6px"}}><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg> 5TH PRIZE</div>
            <div className="pcard-name">Orthopedic Back<br/>Support Prize</div>
            <div className="pcard-sub">&nbsp;</div>
            <span className="pcard-qty">🎁 × 200 Winners</span>
            <div className="pcard-hint">🎯 View &amp; Spin</div>
          </div>
        </div>
      </Link>

    </div>{/*  end .cards-row  */}

  </div>{/*  end .content  */}
</section>
    </div>
  );
};

export default Home;
