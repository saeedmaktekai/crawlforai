# Web Crawler Project

A Python-based asynchronous web crawler that extracts content from websites and saves it in a structured format using the `crawl4ai` library.

## Quick Start

```bash
git clone git@github.com:saeedhumai/crawlforai.git
cd crawl4ai
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py --url "https://saeedanwar.pro"
```

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/crawl4ai.git
cd crawl4ai
```

2. Set up virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Basic usage:

```bash
python main.py --url "https://example.com"
```

Advanced options:

```bash
python main.py \
    --url "https://example.com" \
    --depth 3 \
    --output data.json \
    --concurrent 5 \
    --timeout 30
```


## Project Structure

```
crawl4ai/
├── main.py              # Main crawler script
├── requirements.txt     # Project dependencies
├── output/             # Default output directory
│   └── output.json     # Crawled data
├── tests/              # Test directory
└── README.md           # Documentation
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

