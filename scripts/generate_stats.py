import os
import re
import json
import urllib.request
from datetime import datetime

os.makedirs('assets', exist_ok=True)
USERNAME = 'KshitijShinde26'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

print(f"Fetching statistics for {USERNAME}...")

# 1. Fetch User Data
user_url = f"https://api.github.com/users/{USERNAME}"
try:
    req = urllib.request.Request(user_url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=10) as res:
        user_info = json.loads(res.read().decode())
except Exception as e:
    print("Error fetching user info:", e)
    user_info = {"public_repos": 13, "followers": 1, "created_at": "2024-09-08T00:00:00Z"}

# 2. Fetch Repositories Data
repos_url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100"
try:
    req = urllib.request.Request(repos_url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=10) as res:
        repos_info = json.loads(res.read().decode())
except Exception as e:
    print("Error fetching repos info:", e)
    repos_info = []

total_stars = sum(r.get('stargazers_count', 0) for r in repos_info)
total_forks = sum(r.get('forks_count', 0) for r in repos_info)
total_repos = len(repos_info) if repos_info else user_info.get('public_repos', 13)

# Calculate Languages
lang_counts = {}
for r in repos_info:
    lang = r.get('language')
    if lang:
        lang_counts[lang] = lang_counts.get(lang, 0) + (r.get('size', 100) or 100)

total_lang_weight = sum(lang_counts.values()) or 1
sorted_langs = sorted(lang_counts.items(), key=lambda x: x[1], reverse=True)[:5]

# 3. Fetch Contributions Calendar from GitHub raw page
contrib_url = f"https://github.com/users/{USERNAME}/contributions"
days_data = []
total_contributions = "176"
current_streak = 0
longest_streak = 0

try:
    req = urllib.request.Request(contrib_url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=10) as res:
        html = res.read().decode()

    # Extract total
    match_total = re.search(r'([0-9,]+)\s+contributions\s+in\s+the\s+last\s+year', html)
    if match_total:
        total_contributions = match_total.group(1)

    # Extract day cells: <td ... data-date="YYYY-MM-DD" data-level="0-4" ...>
    day_matches = re.findall(r'data-date="([^"]+)"[^>]*data-level="([^"]+)"', html)
    for d, lvl in day_matches:
        days_data.append((d, int(lvl)))

    # Calculate streaks
    temp_streak = 0
    for _, lvl in days_data:
        if lvl > 0:
            temp_streak += 1
            longest_streak = max(longest_streak, temp_streak)
        else:
            temp_streak = 0
    # Current streak from end
    for _, lvl in reversed(days_data):
        if lvl > 0:
            current_streak += 1
        else:
            break
except Exception as e:
    print("Error parsing contributions:", e)

# -------------------------------------------------------------
# Generate 1: Contribution Graph SVG (Tokyo Night Dark Theme)
# -------------------------------------------------------------
colors = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]  # GitHub contribution levels
# Tokyo night theme palette for calendar
tn_colors = ["#1f2335", "#3b4261", "#7aa2f7", "#7dcfff", "#bb9af7"]

cols = 53
rows = 7
cell_size = 11
cell_gap = 3
start_x = 35
start_y = 45
svg_w = start_x + cols * (cell_size + cell_gap) + 20
svg_h = start_y + rows * (cell_size + cell_gap) + 30

rects_svg = []
months_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
days_labels = ["Mon", "", "Wed", "", "Fri", ""]

# Pad days_data to 53 * 7 = 371
if len(days_data) < 371:
    padding = [("2025-01-01", 0)] * (371 - len(days_data))
    days_data = padding + days_data
elif len(days_data) > 371:
    days_data = days_data[-371:]

for i, (date_str, level) in enumerate(days_data):
    col = i // 7
    row = i % 7
    x = start_x + col * (cell_size + cell_gap)
    y = start_y + row * (cell_size + cell_gap)
    color = tn_colors[min(level, 4)]
    rects_svg.append(f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" rx="2" fill="{color}"><title>{date_str}: Level {level}</title></rect>')

# Month markers
month_svg = []
for m_idx, m_name in enumerate(months_labels):
    m_x = start_x + int(m_idx * (cols / 12) * (cell_size + cell_gap))
    month_svg.append(f'<text x="{m_x}" y="32" fill="#7aa2f7" font-size="10" font-family="Segoe UI, Ubuntu, sans-serif">{m_name}</text>')

contrib_svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}">
  <style>
    .bg {{ fill: #1a1b26; rx: 8px; }}
    .title {{ font: 600 14px 'Segoe UI', Ubuntu, Sans-Serif; fill: #70a5fd; }}
    .sub {{ font: 400 11px 'Segoe UI', Ubuntu, Sans-Serif; fill: #9aa5ce; }}
  </style>
  <rect width="100%" height="100%" class="bg" stroke="#2a2e3f" stroke-width="1" rx="8"/>
  <text x="35" y="20" class="title">Contribution Activity</text>
  <text x="{svg_w - 35}" y="20" class="sub" text-anchor="end">{total_contributions} Contributions in the last year</text>
  {''.join(month_svg)}
  {''.join(rects_svg)}
</svg>'''

with open('assets/github-contribution-graph.svg', 'w', encoding='utf-8') as f:
    f.write(contrib_svg_content)
print("Generated assets/github-contribution-graph.svg")

# -------------------------------------------------------------
# Generate 2: GitHub Stats Card SVG (Dark Theme)
# -------------------------------------------------------------
stats_svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 200" width="380" height="200">
  <style>
    .bg {{ fill: #1a1b26; rx: 8px; }}
    .title {{ font: 600 15px 'Segoe UI', Ubuntu, Sans-Serif; fill: #70a5fd; }}
    .stat-label {{ font: 400 12px 'Segoe UI', Ubuntu, Sans-Serif; fill: #a9b1d6; }}
    .stat-val {{ font: 600 13px 'Segoe UI', Ubuntu, Sans-Serif; fill: #7dcfff; }}
    .icon {{ fill: #7aa2f7; }}
  </style>
  <rect width="100%" height="100%" class="bg" stroke="#2a2e3f" stroke-width="1" rx="8"/>
  <text x="25" y="32" class="title">Kshitij Shinde's GitHub Stats</text>
  
  <g transform="translate(25, 55)">
    <!-- Stars -->
    <text x="25" y="15" class="stat-label">Total Stars Earned:</text>
    <text x="220" y="15" class="stat-val">{total_stars}</text>
    
    <!-- Repositories -->
    <text x="25" y="42" class="stat-label">Public Repositories:</text>
    <text x="220" y="42" class="stat-val">{total_repos}</text>
    
    <!-- Total Contributions -->
    <text x="25" y="69" class="stat-label">Total Contributions:</text>
    <text x="220" y="69" class="stat-val">{total_contributions}</text>
    
    <!-- Primary Focus -->
    <text x="25" y="96" class="stat-label">Primary Direction:</text>
    <text x="220" y="96" class="stat-val" fill="#bb9af7">Java Backend</text>
    
    <!-- Status -->
    <text x="25" y="123" class="stat-label">Development Status:</text>
    <text x="220" y="123" class="stat-val" fill="#9ece6a">Active Building</text>
  </g>
</svg>'''

with open('assets/github-stats.svg', 'w', encoding='utf-8') as f:
    f.write(stats_svg_content)
print("Generated assets/github-stats.svg")

# -------------------------------------------------------------
# Generate 3: Top Languages Card SVG
# -------------------------------------------------------------
lang_colors = {
    "Java": "#b07219",
    "TypeScript": "#3178c6",
    "JavaScript": "#f1e05a",
    "HTML": "#e34c26",
    "CSS": "#563d7c",
    "Jupyter Notebook": "#da5b0b",
}

bars_svg = []
items_svg = []
accum_pct = 0
for idx, (l_name, l_weight) in enumerate(sorted_langs):
    pct = round((l_weight / total_lang_weight) * 100, 1)
    color = lang_colors.get(l_name, "#7aa2f7")
    bars_svg.append(f'<rect x="{accum_pct}%" y="0" width="{pct}%" height="8" fill="{color}"/>')
    accum_pct += pct
    
    col = idx % 2
    row = idx // 2
    item_x = 25 + col * 170
    item_y = 90 + row * 28
    items_svg.append(f'''
      <circle cx="{item_x}" cy="{item_y - 4}" r="5" fill="{color}"/>
      <text x="{item_x + 12}" y="{item_y}" class="stat-label">{l_name}</text>
      <text x="{item_x + 115}" y="{item_y}" class="stat-val">{pct}%</text>
    ''')

langs_svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 200" width="380" height="200">
  <style>
    .bg {{ fill: #1a1b26; rx: 8px; }}
    .title {{ font: 600 15px 'Segoe UI', Ubuntu, Sans-Serif; fill: #70a5fd; }}
    .stat-label {{ font: 400 12px 'Segoe UI', Ubuntu, Sans-Serif; fill: #a9b1d6; }}
    .stat-val {{ font: 600 12px 'Segoe UI', Ubuntu, Sans-Serif; fill: #7dcfff; }}
  </style>
  <rect width="100%" height="100%" class="bg" stroke="#2a2e3f" stroke-width="1" rx="8"/>
  <text x="25" y="32" class="title">Top Languages in Repositories</text>
  
  <g transform="translate(25, 50)">
    <svg width="330" height="8">
      <rect width="100%" height="8" rx="4" fill="#24283b"/>
      <g clip-path="url(#bar-clip)">
        {''.join(bars_svg)}
      </g>
      <clipPath id="bar-clip"><rect width="100%" height="8" rx="4"/></clipPath>
    </svg>
  </g>
  
  {''.join(items_svg)}
</svg>'''

with open('assets/top-languages.svg', 'w', encoding='utf-8') as f:
    f.write(langs_svg_content)
print("Generated assets/top-languages.svg")

# 4. Fetch live streak stats as backup SVG
streak_url = f"https://streak-stats.demolab.com/?user={USERNAME}&theme=dark&hide_border=true"
try:
    req = urllib.request.Request(streak_url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=10) as res:
        streak_data = res.read()
        with open('assets/streak-stats.svg', 'wb') as f:
            f.write(streak_data)
        print("Saved assets/streak-stats.svg from streak-stats.demolab.com")
except Exception as e:
    print("Error fetching streak stats:", e)

print("All stats SVGs generated successfully!")
