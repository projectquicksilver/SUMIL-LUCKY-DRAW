import React, { useState } from 'react';
import Papa from 'papaparse';
import { supabaseAdmin } from '../lib/supabase';
import { Link } from 'react-router-dom';
import './Admin.scss';

const Admin = () => {
  const [uploadStatus, setUploadStatus] = useState({ type: '', msg: '' });
  const [drawStatus, setDrawStatus] = useState({ type: '', msg: '' });
  const [isUploading, setIsUploading] = useState(false);
  const [isDrawing, setIsDrawing] = useState(false);

  const handleUpload = (e) => {
    const file = document.getElementById('csvFile')?.files[0];
    if (!file) {
      setUploadStatus({ type: 'error', msg: 'Please select a CSV file first.' });
      return;
    }

    setIsUploading(true);
    setUploadStatus({ type: 'info', msg: 'Parsing CSV...' });

    Papa.parse(file, {
      header: true,
      skipEmptyLines: true,
      complete: async function(results) {
        try {
          const rawData = results.data;
          const dbRows = [];
          
          for (let row of rawData) {
            if (!row['CUSTOMER CODE']) continue;
            dbRows.push({
              region: row['Region'] || '',
              territory: row['Territory'] || '',
              customer_name: row['CUSTOMER NAME'] || '',
              customer_code: row['CUSTOMER CODE'] || '',
              coupon_code: row['Coupon Codes'] || '',
              phone_number: row['Phone Number'] || '',
              sum_of_max_coupons: parseInt(row['Sum of Max Coupons']) || 0
            });
          }

          setUploadStatus({ type: 'info', msg: 'Clearing old database...' });
          const { error: delErr } = await supabaseAdmin.from('master_customers').delete().neq('id', 0);
          if (delErr) throw delErr;

          setUploadStatus({ type: 'info', msg: 'Inserting new customers...' });
          const batchSize = 1000;
          for (let i = 0; i < dbRows.length; i += batchSize) {
            const batch = dbRows.slice(i, i + batchSize);
            const { error: insErr } = await supabaseAdmin.from('master_customers').insert(batch);
            if (insErr) throw insErr;
          }

          setUploadStatus({ type: 'success', msg: `✅ Successfully synced ${dbRows.length} customers to the database!` });
        } catch (err) {
          console.error(err);
          setUploadStatus({ type: 'error', msg: "Error: " + err.message });
        } finally {
          setIsUploading(false);
          document.getElementById('csvFile').value = '';
        }
      }
    });
  };

  const runDraw = async () => {
    setIsDrawing(true);
    setDrawStatus({ type: 'info', msg: 'Fetching customers...' });

    try {
      const { data: customers, error: fetchErr } = await supabaseAdmin
          .from('master_customers')
          .select('*')
          .gt('sum_of_max_coupons', 0);
      
      if (fetchErr) throw fetchErr;

      let availableCoupons = [...customers];

      const drawQueue = [
          { tier: '5th_prize', count: 200 },
          { tier: '4th_prize', count: 100 },
          { tier: '3rd_prize', count: 50 },
          { tier: 'mega_prize', count: 2 },
          { tier: 'grand_prize', count: 1 }
      ];

      const finalWinners = [];

      for (let draw of drawQueue) {
          const tierWinnerCodes = new Set();

          for (let i = 0; i < draw.count; i++) {
              const eligibleCoupons = availableCoupons.filter(c => !tierWinnerCodes.has(c.customer_code));

              if (eligibleCoupons.length === 0) break;

              const randomIndex = Math.floor(Math.random() * eligibleCoupons.length);
              const winner = eligibleCoupons[randomIndex];
              
              // Remove this specific coupon so it can't be drawn again
              availableCoupons = availableCoupons.filter(c => c.coupon_code !== winner.coupon_code);
              
              tierWinnerCodes.add(winner.customer_code);

              finalWinners.push({
                  prize_tier: draw.tier,
                  region: winner.region,
                  territory: winner.territory,
                  customer_name: winner.customer_name,
                  customer_code: winner.customer_code,
                  coupon_code: winner.coupon_code
              });
          }
      }

      setDrawStatus({ type: 'info', msg: 'Updating Database...' });
      
      const { error: delErr } = await supabaseAdmin.from('draw_winners').delete().neq('id', 0);
      if (delErr) throw delErr;

      if (finalWinners.length > 0) {
          const { error: insErr } = await supabaseAdmin.from('draw_winners').insert(finalWinners);
          if (insErr) throw insErr;
      }

      setDrawStatus({ type: 'success', msg: `✅ Draw Complete! Generated ${finalWinners.length} total winners.` });
    } catch (err) {
      console.error(err);
      setDrawStatus({ type: 'error', msg: "Error: " + err.message });
    } finally {
      setIsDrawing(false);
    }
  };

  return (
    <div id="admin-page">
    <div style={{ backgroundColor: '#020617', color: '#e2e8f0', minHeight: '100vh', padding: '40px', fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif" }}>
      <Link to="/" style={{ color: '#38bdf8', textDecoration: 'none', marginBottom: '20px', display: 'inline-block' }}>← Back to Public Site</Link>
      
      <div style={{ maxWidth: '800px', margin: '0 auto' }}>
        <h1 style={{ color: '#FFD700', textAlign: 'center', marginBottom: '10px' }}>Admin Control Portal</h1>
        <p style={{ textAlign: 'center', color: '#94a3b8', marginBottom: '40px' }}>100% Serverless. Direct Database Connection.</p>
        
        <div style={{ background: '#0f172a', border: '1px solid #1e293b', borderRadius: '12px', padding: '25px', marginBottom: '25px' }}>
          <h2 style={{ marginTop: 0, color: '#38bdf8', fontSize: '22px' }}>1. Upload Master Data</h2>
          <p style={{ color: '#94a3b8', fontSize: '15px', marginBottom: '20px' }}>Select your <b>master_data.csv</b> file. This will wipe the old database and upload these customers into the <b>master_customers</b> table.</p>
          <input type="file" id="csvFile" accept=".csv" style={{ marginBottom: '15px' }} />
          
          <button 
            onClick={handleUpload} 
            disabled={isUploading}
            style={{ display: 'block', width: '100%', padding: '15px', fontSize: '20px', fontWeight: 'bold', border: 'none', borderRadius: '8px', cursor: isUploading ? 'not-allowed' : 'pointer', background: isUploading ? '#475569' : '#0284c7', color: 'white' }}
          >
            {isUploading ? uploadStatus.msg : '📤 Upload & Sync to Database'}
          </button>
          
          {uploadStatus.msg && !isUploading && (
            <div style={{ marginTop: '15px', fontWeight: 'bold', color: uploadStatus.type === 'error' ? '#ef4444' : '#10b981' }}>
              {uploadStatus.msg}
            </div>
          )}
        </div>

        <div style={{ background: '#0f172a', border: '1px solid #1e293b', borderRadius: '12px', padding: '25px', marginBottom: '25px' }}>
          <h2 style={{ marginTop: 0, color: '#38bdf8', fontSize: '22px' }}>2. Execute the Lucky Draw</h2>
          <p style={{ color: '#94a3b8', fontSize: '15px', marginBottom: '20px' }}>This runs the weighted algorithm, completely clearing old winners and inserting the 353 new winners directly into the <b>draw_winners</b> database table.</p>
          
          <button 
            onClick={runDraw} 
            disabled={isDrawing}
            style={{ display: 'block', width: '100%', padding: '15px', fontSize: '20px', fontWeight: 'bold', border: 'none', borderRadius: '8px', cursor: isDrawing ? 'not-allowed' : 'pointer', background: isDrawing ? '#475569' : 'linear-gradient(135deg, #C0000A, #FF4500)', color: 'white' }}
          >
            {isDrawing ? drawStatus.msg : '🎲 Run Algorithm & Draw Winners'}
          </button>
          
          {drawStatus.msg && !isDrawing && (
            <div style={{ marginTop: '15px', fontWeight: 'bold', color: drawStatus.type === 'error' ? '#ef4444' : '#10b981' }}>
              {drawStatus.msg}
            </div>
          )}
        </div>
        
      </div>
    </div>
    </div>
  );
};

export default Admin;
