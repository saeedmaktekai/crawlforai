import os
from datetime import datetime
from crawl4ai import AsyncWebCrawler, CacheMode
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

# Create a model for the URL input
class CrawlRequest(BaseModel):
    url: str

@app.post("/crawl")
async def crawl_and_download(request: CrawlRequest):
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url=request.url)
    
        # Generate unique filename using timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"crawl_result_{timestamp}.txt"
        
        # Ensure 'results' directory exists
        os.makedirs('results', exist_ok=True)
        
        file_path = f"results/{filename}"
        
        # Save the results in a structured format
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("=" * 50 + "\n")
            f.write("Web Crawl Results\n")
            f.write(f"URL: {request.url}\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 50 + "\n\n")
            
            # Write the markdown content with proper formatting
            f.write("Content:\n")
            f.write("-" * 50 + "\n")
            f.write(result.markdown)
            f.write("\n" + "-" * 50 + "\n")
        
        # Return the file as a forced download
        return FileResponse(
            path=file_path,
            filename=filename,
            media_type='text/plain',
            content_disposition_type='attachment'
        )

if __name__ == "__main__":
    asyncio.run(main())
    