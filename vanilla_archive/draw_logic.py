import csv
import random
import os

def draw_all_winners(master_csv_path, output_dir):
    # Load master data
    customers = {}
    
    with open(master_csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            code = row.get('CUSTOMER CODE', '').strip()
            if not code:
                continue
            
            try:
                coupons = int(row.get('Sum of Max Coupons', 0))
            except ValueError:
                coupons = 0
                
            if coupons > 0:
                customers[code] = {
                    'Region': row.get('Region', '').strip(),
                    'Territory': row.get('Territory', '').strip(),
                    'CUSTOMER NAME': row.get('CUSTOMER NAME', '').strip(),
                    'CUSTOMER CODE': code,
                    'coupons': coupons
                }

    # Define the prize draw order (Bottom-up as requested by user)
    draw_queue = [
        ('5th_prize.csv', 200),        # 5th Prize
        ('4th_prize.csv', 100),        # 4th Prize
        ('3rd_prize.csv', 50),         # 3rd Prize
        ('mega_prize.csv', 2),         # Mega Prize
        ('grand_prize.csv', 1)         # Grand Prize
    ]
    
    results = {}

    for filename, winner_count in draw_queue:
        tier_winners = []
        tier_winner_codes = set()
        
        for _ in range(winner_count):
            # Build eligible pool for this specific draw
            eligible_codes = []
            eligible_weights = []
            
            for code, data in customers.items():
                if data['coupons'] > 0 and code not in tier_winner_codes:
                    eligible_codes.append(code)
                    eligible_weights.append(data['coupons'])
            
            if not eligible_codes:
                # Not enough unique eligible winners left
                break
                
            # Random weighted choice
            winner_code = random.choices(eligible_codes, weights=eligible_weights, k=1)[0]
            
            # Deduct coupon
            customers[winner_code]['coupons'] -= 1
            
            # Add to tier winners
            tier_winner_codes.add(winner_code)
            winner_data = customers[winner_code]
            
            # Format according to front-end expectations (name, mobile, district, state)
            tier_winners.append([
                winner_data['CUSTOMER NAME'],
                winner_data['CUSTOMER CODE'],
                winner_data['Territory'],
                winner_data['Region']
            ])
            
        results[filename] = tier_winners
        
        # Write to file immediately
        out_path = os.path.join(output_dir, filename)
        with open(out_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["CUSTOMER NAME", "CUSTOMER CODE", "Territory", "Region"])
            for row in tier_winners:
                writer.writerow(row)
                
    return results

if __name__ == '__main__':
    # Test script standalone
    base_dir = '/Users/ankush/Desktop/Sumil Lucky Draw'
    master_csv = os.path.join(base_dir, 'master_data.csv')
    res = draw_all_winners(master_csv, base_dir)
    print("Draw complete. File outputs generated:")
    for k, v in res.items():
        print(f"{k}: {len(v)} winners")
