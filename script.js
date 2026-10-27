// Ms.Porn Slushie - Buriram Shop & Local Factory Interactions

document.addEventListener('DOMContentLoaded', () => {
  // Initialize Lucide Icons
  if (window.lucide) {
    lucide.createIcons();
  }

  // Mobile Menu Toggle
  const mobileMenuBtn = document.getElementById('mobileMenuBtn');
  const mobileMenu = document.getElementById('mobileMenu');
  const menuIcon = document.getElementById('menuIcon');

  if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener('click', () => {
      const isHidden = mobileMenu.classList.contains('hidden');
      if (isHidden) {
        mobileMenu.classList.remove('hidden');
        menuIcon.setAttribute('data-lucide', 'x');
      } else {
        mobileMenu.classList.add('hidden');
        menuIcon.setAttribute('data-lucide', 'menu');
      }
      lucide.createIcons();
    });

    // Close mobile menu when a navigation item is clicked
    document.querySelectorAll('.mobile-nav-link').forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.add('hidden');
        menuIcon.setAttribute('data-lucide', 'menu');
        lucide.createIcons();
      });
    });
  }
});

// Interactive Delivery Radius Checker (Buriram 20km)
function checkLocation(landmarkName, distanceKm) {
  // Highlight active chip
  document.querySelectorAll('.landmark-chip').forEach(btn => {
    btn.classList.remove('active');
  });

  const targetBtn = Array.from(document.querySelectorAll('.landmark-chip')).find(b => b.textContent.includes(landmarkName));
  if (targetBtn) {
    targetBtn.classList.add('active');
  }

  const resultContainer = document.getElementById('checkResult');
  const resultTitle = document.getElementById('resultTitle');
  const resultDesc = document.getElementById('resultDesc');

  if (!resultContainer) return;

  if (distanceKm <= 20) {
    resultContainer.className = 'p-4 rounded-2xl bg-emerald-50 border border-emerald-200 text-emerald-900 transition-all';
    resultTitle.innerHTML = `✅ ${landmarkName} (~${distanceKm} km) is within our 20km Delivery Zone!`;
    resultDesc.innerHTML = `Great news! We deliver direct to this area in Buriram with thermal ice-pack insulation. Call <strong>086-557-8822</strong> to order your ice-cold cups now!`;
  } else {
    resultContainer.className = 'p-4 rounded-2xl bg-amber-50 border border-amber-200 text-amber-900 transition-all';
    resultTitle.innerHTML = `⚠️ ${landmarkName} (~${distanceKm} km) is beyond our standard 20km delivery zone`;
    resultDesc.innerHTML = `Our standard fast delivery is within 20km in Buriram. For bulk or special party orders further out, please call <strong>086-557-8822</strong> to arrange special transport.`;
  }

  if (window.lucide) {
    lucide.createIcons();
  }
}

// Custom location query checker
function checkCustomLocation() {
  const input = document.getElementById('customLocationInput');
  const query = input ? input.value.trim().toLowerCase() : '';
  const resultContainer = document.getElementById('checkResult');
  const resultTitle = document.getElementById('resultTitle');
  const resultDesc = document.getElementById('resultDesc');

  if (!query) {
    alert('Please enter a location name or distance in kilometers.');
    return;
  }

  // Clear chip selections
  document.querySelectorAll('.landmark-chip').forEach(btn => btn.classList.remove('active'));

  // Check if user input a number (e.g. "12", "12km", "25 km")
  const numberMatch = query.match(/(\d+(\.\d+)?)/);
  if (numberMatch) {
    const km = parseFloat(numberMatch[0]);
    if (km <= 20) {
      resultContainer.className = 'p-4 rounded-2xl bg-emerald-50 border border-emerald-200 text-emerald-900 transition-all';
      resultTitle.innerHTML = `✅ ${km} km from Ms.Porn Slushie: Within 20km Delivery Area!`;
      resultDesc.innerHTML = `Your destination is covered by our local Buriram delivery route. Call <strong>086-557-8822</strong> for fresh cups dispatched promptly.`;
    } else {
      resultContainer.className = 'p-4 rounded-2xl bg-amber-50 border border-amber-200 text-amber-900 transition-all';
      resultTitle.innerHTML = `⚠️ ${km} km is beyond our standard 20km delivery radius`;
      resultDesc.innerHTML = `For destinations beyond 20km in Buriram, please call <strong>086-557-8822</strong> to check if special insulated bulk arrangements are possible.`;
    }
  } else {
    // If text location in Buriram
    resultContainer.className = 'p-4 rounded-2xl bg-emerald-50 border border-emerald-200 text-emerald-900 transition-all';
    resultTitle.innerHTML = `📍 Checking "${query}" in Buriram`;
    resultDesc.innerHTML = `Most areas around Mueang Buriram and neighboring subdistricts fall within our 20km boundary! Give us a quick ring at <a href="tel:0865578822" class="underline font-bold text-brand">086-557-8822</a> to verify exact road coordinates.`;
  }

  if (window.lucide) {
    lucide.createIcons();
  }
}

// Order a specific flavor directly from flavor cards
function requestFlavorOrder(flavorName) {
  const flavorSelect = document.getElementById('orderFlavor');
  const contactSection = document.getElementById('contact');
  const addressInput = document.getElementById('orderAddress');

  if (flavorSelect) {
    // Attempt to match option
    for (let i = 0; i < flavorSelect.options.length; i++) {
      if (flavorSelect.options[i].text.toLowerCase().includes(flavorName.split(' ')[0].toLowerCase())) {
        flavorSelect.selectedIndex = i;
        break;
      }
    }
  }

  if (contactSection) {
    contactSection.scrollIntoView({ behavior: 'smooth' });
    setTimeout(() => {
      if (addressInput) {
        addressInput.focus();
      }
    }, 600);
  }
}

// Copy phone number function
function copyPhoneNumber() {
  const phoneNumber = '0865578822';
  navigator.clipboard.writeText(phoneNumber).then(() => {
    const copyBtnText = document.getElementById('copyBtnText');
    if (copyBtnText) {
      const original = copyBtnText.textContent;
      copyBtnText.textContent = 'Copied: 086-557-8822!';
      setTimeout(() => {
        copyBtnText.textContent = original;
      }, 2500);
    }
  }).catch(() => {
    alert('Phone: 086-557-8822');
  });
}

// Quick Order Form submission
function handleOrderSubmit(event) {
  event.preventDefault();

  const name = document.getElementById('orderName').value.trim();
  const phone = document.getElementById('orderPhone').value.trim();
  const flavor = document.getElementById('orderFlavor').value;
  const address = document.getElementById('orderAddress').value.trim();
  const notes = document.getElementById('orderNotes').value.trim();

  const toast = document.getElementById('formSuccessToast');
  if (toast) {
    toast.innerHTML = `
      <strong>✨ Order Prepared for ${name}!</strong><br>
      Flavor: ${flavor}<br>
      Buriram Address: ${address} (Within 20km)<br>
      <div class="mt-2">
        <a href="tel:0865578822" class="inline-flex items-center gap-1 font-bold text-brand underline text-xs">
          📞 Tap to Call 086-557-8822 & Confirm Now
        </a>
      </div>
    `;
    toast.classList.remove('hidden');
    toast.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  // Open telephone dialer automatically after short delay
  setTimeout(() => {
    if (confirm(`Would you like to dial Ms.Porn Slushie (086-557-8822) now to place this order?`)) {
      window.location.href = 'tel:0865578822';
    }
  }, 700);
}
