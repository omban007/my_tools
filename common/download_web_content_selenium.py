from selenium import webdriver

def save_website_content(url, save_path):
    # Set up the webdriver (you need to have a WebDriver executable, like chromedriver, in your PATH)
    driver = webdriver.Chrome()

    try:
        # Navigate to the specified URL
        driver.get(url)

        # Get the page content
        page_content = driver.page_source

        # Save the content to a file
        with open(save_path, 'w', encoding='utf-8') as file:
            file.write(page_content)

        print(f"Website content saved to: {save_path}")

    finally:
        # Close the webdriver
        driver.quit()

# Example usage
website_url = 'https://example.com'
output_path = 'website_content.html'
save_website_content(website_url, output_path)
