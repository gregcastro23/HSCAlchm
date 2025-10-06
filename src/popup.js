// Check if we're in a Chrome extension environment
if (typeof chrome !== 'undefined' && chrome.runtime && chrome.runtime.id) {
  // Your extension code here
  chrome.storage.local.get(['recipes'], function(_result) {
    // Handle recipe data
  });
} else {
  console.warn('Not running in Chrome extension context');
}
