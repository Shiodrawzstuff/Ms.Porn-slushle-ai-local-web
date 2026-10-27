import subprocess
import json
import re

html_with_inspector = """
<!DOCTYPE html>
<html>
<body>
<script>
window.onload = function() {
  const data = {
    // Nav elements
    navPhone: getRect('header a[href*="0865578822"]'),
    navOrder: getRect('header a[href*="delivery"]'),
    // Hero elements
    heroCheckDelivery: getRect('#home a[href*="delivery-checker"]'),
    heroPhone: getRect('#home a[href*="0865578822"]'),
    heroCard: getRect('#home .shadow-cozy-lg'),
    // Flavors elements
    flavorsHeader: getRect('#flavors h2'),
    orangeCard: getRect('#flavors .flavor-card:first-child'),
    orangeOrderBtn: getRect('#flavors .flavor-card:first-child button'),
    // Delivery elements
    deliverySection: getRect('#delivery'),
    landmarkChips: getRect('#landmarkChips'),
    customInput: getRect('#customLocationInput'),
    checkBtn: getRect('#delivery-checker button.bg-brand'),
    resultBox: getRect('#checkResult'),
    // Location section
    locationSection: getRect('#location'),
    mapBtn: getRect('#location a[href*="maps"]'),
    // Contact section
    contactSection: getRect('#contact'),
    contactCallBtn: getRect('#contact a.bg-brand'),
    copyPhoneBtn: getRect('#copyBtn'),
    orderForm: getRect('#quickOrderForm'),
    orderSubmitBtn: getRect('#quickOrderForm button[type="submit"]')
  };
  function getRect(sel) {
    const el = document.querySelector(sel);
    if (!el) return null;
    const r = el.getBoundingClientRect();
    return { x: Math.round(r.left), y: Math.round(r.top + window.scrollY), w: Math.round(r.width), h: Math.round(r.height) };
  }
  document.title = "RECTS:" + JSON.stringify(data);
};
</script>
</body>
</html>
"""

# Let's inspect the page in Chrome and read title or output
print("Checking rects...")
