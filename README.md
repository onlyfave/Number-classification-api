# Number Classification API

## Overview
The **Number Classification API** is a FastAPI-powered web service that classifies numbers based on their mathematical properties and provides a fun fact. It determines whether a number is **prime**, **perfect**, **Armstrong**, **even**, or **odd** and fetches an interesting fact from an external API.

## Features
- Classifies numbers based on mathematical properties.
- Fetches fun facts using the [Numbers API](http://numbersapi.com/).
- Provides a structured JSON response.
- Handles errors gracefully and ensures valid integer input.
- Publicly accessible and deployed on **Google Cloud Compute Engine (GCE)**.

## API Endpoint
### **Classify a Number**
**GET** `/api/classify-number?number=<integer>`

#### **Request Parameters**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `number`  | int  | Yes      | The number to classify |

#### **Successful Response (200 OK)**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### **Error Response (400 Bad Request)**
```json
{
    "number": "abc",
    "error": true,
    "message": "Invalid input. Please enter an integer."
}
```

## Deployment Details
- **Framework**: FastAPI (Python)
- **Hosting Platform**: Google Cloud Compute Engine (GCE)
- **Port**: 8000
- **CORS Handling**: Enabled to allow cross-origin requests

## Installation & Setup
### **Prerequisites**
- Python 3.8+
- FastAPI & Uvicorn
- Virtual Environment (optional but recommended)

### **Steps to Run Locally**
```bash
# Clone the repository
git clone https://github.com/onlyfave/Number-classification-api.git
cd Number-classification-api

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Deployment on Google Cloud Compute Engine (GCE)
1. **Create a VM Instance** on GCE.
2. **Install dependencies**:
   ```bash
   sudo apt update && sudo apt install python3-pip
   pip install fastapi uvicorn
   ```
3. **Run the API in the background**:
   ```bash
   nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
   ```
4. **Allow external traffic** on port 8000:
   ```bash
   gcloud compute firewall-rules create allow-fastapi \
       --allow tcp:8000 \
       --target-tags=http-server \
       --description="Allow FastAPI traffic"
   ```
5. **Verify API is accessible**:
   ```bash
   curl http://<your-external-ip>:8000/
   ```

## Project Structure
```
Number-classification-api/
│── main.py               # FastAPI application
│── requirements.txt      # Project dependencies
│── README.md             # Documentation (this file)
└── .gitignore            # Git ignore file
```

## Testing the API
You can test the API using **cURL**, **Postman**, or a web browser:
```bash
curl "http://35.209.49.217:8000/api/classify-number?number=42"
```

## Author
- **Favour Onyenkefe**  
- GitHub: [onlyfave](https://github.com/onlyfave)
- Twitter: [@onlyfave](https://twitter.com/onlyfave)

## License
This project is licensed under the MIT License.

## Conclusion
The **Number Classification API** is a lightweight and efficient API that provides mathematical insights and fun facts about numbers. Future improvements may include support for additional number properties and performance optimizations.

