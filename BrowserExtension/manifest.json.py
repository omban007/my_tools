// manifest.json
{
  "manifest_version": 2,
  "name": "Website Content Saver",
  "version": "1.0",
  "description": "Save the content of the currently opened website.",
  "permissions": ["activeTab", "storage"],
  "browser_action": {
    "default_icon": "icon.png",
    "default_popup": "popup.html"
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"]
    }
  ]
}
