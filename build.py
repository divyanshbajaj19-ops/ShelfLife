import os
import re

base_dir = r"c:\Users\divya\OneDrive\Desktop\ShelfLife"
out_dir = os.path.join(base_dir, "ShelfLifeWebsite")

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

pages = {
    "home_shelf_life": "index.html",
    "about_us_shelf_life": "about.html",
    "contact_shelf_life": "contact.html",
    "dashboard_shelf_life": "dashboard.html",
    "features_shelf_life": "features.html",
    "pricing_shelf_life": "pricing.html",
}

AUTH_BLOCK = """
    <!-- Auth Modal (injected by build.py) -->
    <div id="auth-modal" style="display:none;position:fixed;inset:0;background:rgba(0,0,0,0.5);z-index:1000;align-items:center;justify-content:center;backdrop-filter:blur(4px);">
        <div style="background:rgba(255,255,255,0.97);border-radius:1rem;padding:2rem;width:100%;max-width:420px;position:relative;box-shadow:0 8px 32px rgba(0,0,0,0.15);">
            <button id="close-modal" onclick="document.getElementById('auth-modal').style.display='none'" style="position:absolute;top:1rem;right:1rem;background:none;border:none;cursor:pointer;font-size:1.25rem;color:#6b7280;">&times;</button>
            <h2 id="auth-title" style="font-size:1.4rem;font-weight:700;margin-bottom:1.5rem;text-align:center;color:#0f172a;">Login to Shelf-Life</h2>
            <div id="auth-error" style="display:none;margin-bottom:1rem;padding:0.75rem;background:#fee2e2;color:#b91c1c;border-radius:0.5rem;font-size:0.875rem;"></div>
            <div id="auth-success" style="display:none;margin-bottom:1rem;padding:0.75rem;background:#dcfce7;color:#15803d;border-radius:0.5rem;font-size:0.875rem;"></div>
            <form id="auth-form" onsubmit="handleAuthSubmit(event)" style="display:flex;flex-direction:column;gap:1rem;">
                <div>
                    <label style="display:block;font-size:0.875rem;font-weight:500;color:#374151;margin-bottom:0.25rem;">Email</label>
                    <input type="email" id="auth-email" required style="width:100%;padding:0.5rem 1rem;border:1px solid #d1d5db;border-radius:0.5rem;outline:none;color:#0f172a;background:white;box-sizing:border-box;">
                </div>
                <div>
                    <label style="display:block;font-size:0.875rem;font-weight:500;color:#374151;margin-bottom:0.25rem;">Password</label>
                    <input type="password" id="auth-password" required style="width:100%;padding:0.5rem 1rem;border:1px solid #d1d5db;border-radius:0.5rem;outline:none;color:#0f172a;background:white;box-sizing:border-box;">
                </div>
                <button type="submit" id="auth-submit" style="width:100%;background:#006e2f;color:white;padding:0.6rem;border-radius:0.5rem;font-weight:700;border:none;cursor:pointer;font-size:1rem;">Login</button>
            </form>
            <p style="margin-top:1rem;text-align:center;font-size:0.875rem;color:#4b5563;">
                <span id="auth-switch-text">Don't have an account?</span>
                <button id="switch-auth-mode" onclick="toggleAuthMode()" style="color:#006e2f;font-weight:700;background:none;border:none;cursor:pointer;">Sign Up</button>
            </p>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
    <script>
        const _supabase = supabase.createClient(
            'https://eekpybvlcpvwluxqfzsx.supabase.co',
            'sb_publishable_QkP3goJTdD6UJUi7-MoDMg_CYvzdyzi'
        );
        let _isLogin = true;

        function openAuthModal(mode) {
            _isLogin = (mode === 'login');
            document.getElementById('auth-title').innerText = _isLogin ? 'Login to Shelf-Life' : 'Sign Up for Shelf-Life';
            document.getElementById('auth-submit').innerText = _isLogin ? 'Login' : 'Sign Up';
            document.getElementById('auth-switch-text').innerText = _isLogin ? "Don't have an account?" : "Already have an account?";
            document.getElementById('switch-auth-mode').innerText = _isLogin ? 'Sign Up' : 'Login';
            document.getElementById('auth-error').style.display = 'none';
            document.getElementById('auth-success').style.display = 'none';
            document.getElementById('auth-form').reset();
            document.getElementById('auth-modal').style.display = 'flex';
        }

        function toggleAuthMode() { openAuthModal(_isLogin ? 'signup' : 'login'); }

        document.getElementById('auth-modal').addEventListener('click', function(e) {
            if (e.target === this) this.style.display = 'none';
        });

        async function handleAuthSubmit(e) {
            e.preventDefault();
            const errEl = document.getElementById('auth-error');
            const sucEl = document.getElementById('auth-success');
            const btn = document.getElementById('auth-submit');
            errEl.style.display = 'none'; sucEl.style.display = 'none';
            btn.disabled = true; btn.innerText = 'Processing...';
            const email = document.getElementById('auth-email').value;
            const password = document.getElementById('auth-password').value;
            try {
                if (_isLogin) {
                    const { error } = await _supabase.auth.signInWithPassword({ email, password });
                    if (error) throw error;
                    // Redirect to dashboard after successful login
                    window.location.href = 'dashboard.html';
                } else {
                    const { error } = await _supabase.auth.signUp({ email, password });
                    if (error) throw error;
                    sucEl.innerText = 'Account created! Check your email to verify, then log in.';
                    sucEl.style.display = 'block';
                }
            } catch (err) {
                errEl.innerText = err.message;
                errEl.style.display = 'block';
            } finally {
                btn.disabled = false;
                btn.innerText = _isLogin ? 'Login' : 'Sign Up';
            }
        }

        async function checkAuthSession() {
            const { data: { session } } = await _supabase.auth.getSession();
            const loginBtn = document.getElementById('nav-login-btn');
            const signupBtn = document.getElementById('nav-signup-btn');
            if (session) {
                if (loginBtn) loginBtn.style.display = 'none';
                if (signupBtn) {
                    signupBtn.innerText = 'Log Out';
                    signupBtn.style.background = '#ba1a1a';
                    signupBtn.onclick = () => _supabase.auth.signOut().then(() => location.reload());
                }
                const dashLink = document.getElementById('nav-dashboard-link');
                if (dashLink) dashLink.style.display = 'block';
                const h1 = document.querySelector('main h1');
                if (h1 && session.user.email) {
                    const u = session.user.email.split('@')[0];
                    h1.innerText = 'Namaste, ' + u.charAt(0).toUpperCase() + u.slice(1);
                }
            } else {
                if (loginBtn) loginBtn.onclick = () => openAuthModal('login');
                if (signupBtn) signupBtn.onclick = () => openAuthModal('signup');
            }
        }
        checkAuthSession();
    </script>
"""

for folder, out_file in pages.items():
    code_path = os.path.join(base_dir, folder, "code.html")
    if not os.path.exists(code_path):
        print(f"Skipping {folder}, code.html not found.")
        continue
    
    with open(code_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace nav links
    content = re.sub(r'href="[^"]*"([^>]*>Home</a>)', r'href="index.html"\1', content, flags=re.IGNORECASE)
    content = re.sub(r'href="[^"]*"([^>]*>Features</a>)', r'href="features.html"\1', content, flags=re.IGNORECASE)
    content = re.sub(r'href="[^"]*"([^>]*>Pricing</a>)', r'href="pricing.html"\1', content, flags=re.IGNORECASE)
    content = re.sub(r'href="[^"]*"([^>]*>About</a>)', r'href="about.html"\1', content, flags=re.IGNORECASE)
    content = re.sub(r'href="[^"]*"([^>]*>Contact</a>)', r'href="contact.html"\1', content, flags=re.IGNORECASE)

    # Insert Dashboard link after About link
    content = re.sub(
        r'(<a[^>]*href="about\.html"[^>]*>About</a>)',
        r'\1\n<a id="nav-dashboard-link" class="text-slate-600 dark:text-slate-400 hover:text-green-600 dark:hover:text-green-400 transition-colors font-body-sm font-medium" style="display: none;" href="dashboard.html">Dashboard</a>',
        content, flags=re.IGNORECASE
    )

    # Link the brand logo text to home
    content = re.sub(r'(<div[^>]*>)\s*Shelf-Life\s*(</div>)', r'\1<a href="index.html" style="text-decoration:none;color:inherit;">Shelf-Life</a>\2', content)

    # Footer links
    content = re.sub(r'href="[^"]*"([^>]*>About Us</a>)', r'href="about.html"\1', content, flags=re.IGNORECASE)

    # Add IDs to Login and Sign Up buttons so auth modal JS can find them
    # Only add ID if the button doesn't already have one
    content = re.sub(
        r'<button(?![^>]*\bid=)((?:[^>]*))>\s*Login\s*</button>',
        r'<button id="nav-login-btn"\1>Login</button>',
        content, flags=re.IGNORECASE
    )
    content = re.sub(
        r'<button(?![^>]*\bid=)((?:[^>]*))>\s*Sign\s*Up\s*</button>',
        r'<button id="nav-signup-btn"\1>Sign Up</button>',
        content, flags=re.IGNORECASE
    )

    # Inject auth block before </body> — skip dashboard since it has its own auth
    if folder != "dashboard_shelf_life":
        content = content.replace("</body>", AUTH_BLOCK + "\n</body>", 1)

    out_path = os.path.join(out_dir, out_file)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Generated {out_file}")

print("Build complete.")
