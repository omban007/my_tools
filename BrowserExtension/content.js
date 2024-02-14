// content.js
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.action === 'saveContent') {
    const content = document.documentElement.outerHTML;
    chrome.storage.local.set({ 'savedContent': content }, function () {
      console.log('Content saved.');
    });
  }
});
