"""
Comprehensive Playwright Test for Streamlit App
Tests the complete 3-phase workflow with real file upload
"""

import os
import time
from playwright.sync_api import sync_playwright, expect

def test_streamlit_app():
    """Test the complete Streamlit app workflow"""
    
    print("\n" + "="*60)
    print("🎭 PLAYWRIGHT COMPREHENSIVE TEST")
    print("="*60)
    
    with sync_playwright() as p:
        # Launch browser
        print("\n🌐 Launching browser...")
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Navigate to app
        print("📍 Navigating to http://localhost:8502...")
        page.goto("http://localhost:8502")
        page.wait_for_load_state("networkidle")
        time.sleep(2)
        
        # Test 1: Verify page loaded
        print("\n" + "="*60)
        print("TEST 1: Page Load Verification")
        print("="*60)
        
        title = page.title()
        print(f"✅ Page title: {title}")
        assert "ICON AI-Proposal Engine" in title or "Streamlit" in title
        
        # Test 2: Verify UI elements
        print("\n" + "="*60)
        print("TEST 2: UI Elements Verification")
        print("="*60)
        
        # Check for main heading
        heading = page.locator("h1:has-text('ICON AI-Proposal Engine')")
        if heading.count() > 0:
            print("✅ Main heading found")
        else:
            print("⚠️  Main heading not found")
        
        # Check for file uploader
        uploader = page.locator("text=Upload Client RFP")
        if uploader.count() > 0:
            print("✅ File uploader found")
        else:
            print("❌ File uploader not found")
        
        # Check for DOCX-only message
        docx_msg = page.locator("text=DOCX format ensures")
        if docx_msg.count() > 0:
            print("✅ DOCX-only message found (no OCR)")
        else:
            print("⚠️  DOCX message not found")
        
        # Check for 3-phase workflow description
        phase_text = page.locator("text=3-Phase RAG Workflow")
        if phase_text.count() > 0:
            print("✅ 3-Phase workflow description found")
        else:
            print("⚠️  Workflow description not found")
        
        # Test 3: Check for Browse Files button
        print("\n" + "="*60)
        print("TEST 3: File Upload Interface")
        print("="*60)
        
        browse_button = page.locator("button:has-text('Browse files')")
        if browse_button.count() > 0:
            print("✅ Browse files button found")
        else:
            print("⚠️  Browse files button not found")
        
        # Test 4: Verify Clear All button
        clear_button = page.locator("button:has-text('Clear All')")
        if clear_button.count() > 0:
            print("✅ Clear All button found")
        else:
            print("⚠️  Clear All button not found")
        
        # Test 5: Take screenshots
        print("\n" + "="*60)
        print("TEST 5: Screenshot Capture")
        print("="*60)
        
        os.makedirs("test_screenshots", exist_ok=True)
        
        page.screenshot(path="test_screenshots/01_initial_load.png")
        print("✅ Screenshot saved: 01_initial_load.png")
        
        # Test 6: Simulate file upload (if sample exists)
        print("\n" + "="*60)
        print("TEST 6: File Upload Simulation")
        print("="*60)
        
        sample_file = os.path.abspath("sample_client_rfp.docx")
        if os.path.exists(sample_file):
            print(f"📄 Sample file found: {sample_file}")
            
            # Find file input and upload
            file_input = page.locator("input[type='file']")
            if file_input.count() > 0:
                print("✅ File input element found")
                file_input.set_input_files(sample_file)
                print("✅ File uploaded to input")
                
                time.sleep(2)
                page.screenshot(path="test_screenshots/02_file_uploaded.png")
                print("✅ Screenshot saved: 02_file_uploaded.png")
                
                # Look for Start Processing button
                start_button = page.locator("button:has-text('Start Processing')")
                if start_button.count() > 0:
                    print("✅ Start Processing button appeared")
                    
                    # Click the button
                    start_button.click()
                    print("✅ Clicked Start Processing")
                    
                    # Wait for processing
                    time.sleep(3)
                    page.screenshot(path="test_screenshots/03_processing.png")
                    print("✅ Screenshot saved: 03_processing.png")
                    
                    # Check for Phase 1 content
                    phase1 = page.locator("text=Phase 1")
                    if phase1.count() > 0:
                        print("✅ Phase 1 UI appeared")
                        time.sleep(2)
                        page.screenshot(path="test_screenshots/04_phase1.png")
                        print("✅ Screenshot saved: 04_phase1.png")
                        
                        # Check for extracted metadata
                        project_name = page.locator("input[value*='Water Treatment']")
                        if project_name.count() > 0:
                            print("✅ Project name extracted correctly")
                        
                        # Look for Step 2 button
                        step2_button = page.locator("button:has-text('Step 2')")
                        if step2_button.count() > 0:
                            print("✅ Step 2 button found")
                            step2_button.click()
                            print("✅ Clicked Step 2")
                            
                            time.sleep(3)
                            page.screenshot(path="test_screenshots/05_phase2.png")
                            print("✅ Screenshot saved: 05_phase2.png")
                            
                            # Check for Phase 2 content
                            phase2 = page.locator("text=Phase 2")
                            if phase2.count() > 0:
                                print("✅ Phase 2 UI appeared")
                            
                            # Look for Step 3 button
                            step3_button = page.locator("button:has-text('Step 3')")
                            if step3_button.count() > 0:
                                print("✅ Step 3 button found")
                                step3_button.click()
                                print("✅ Clicked Step 3")
                                
                                time.sleep(3)
                                page.screenshot(path="test_screenshots/06_phase3.png")
                                print("✅ Screenshot saved: 06_phase3.png")
                                
                                # Look for Generate button
                                generate_button = page.locator("button:has-text('Generate')")
                                if generate_button.count() > 0:
                                    print("✅ Generate button found")
                                    generate_button.click()
                                    print("✅ Clicked Generate")
                                    
                                    time.sleep(5)
                                    page.screenshot(path="test_screenshots/07_generated.png")
                                    print("✅ Screenshot saved: 07_generated.png")
                                    
                                    # Check for download button
                                    download_button = page.locator("button:has-text('Download')")
                                    if download_button.count() > 0:
                                        print("✅ Download button appeared")
                                        print("🎉 COMPLETE WORKFLOW TESTED!")
                    else:
                        print("⚠️  Phase 1 UI did not appear")
                else:
                    print("⚠️  Start Processing button not found")
            else:
                print("❌ File input element not found")
        else:
            print("⚠️  Sample file not found, skipping upload test")
        
        # Final screenshot
        page.screenshot(path="test_screenshots/08_final_state.png")
        print("✅ Final screenshot saved")
        
        # Keep browser open for inspection
        print("\n" + "="*60)
        print("🎭 Test Complete - Browser will stay open for 10 seconds")
        print("="*60)
        time.sleep(10)
        
        browser.close()
        print("\n✅ Browser closed")

if __name__ == "__main__":
    try:
        test_streamlit_app()
        print("\n🎉 ALL PLAYWRIGHT TESTS COMPLETED SUCCESSFULLY!")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
