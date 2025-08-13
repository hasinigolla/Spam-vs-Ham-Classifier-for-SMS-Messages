# spam_ham_aws_app.py
import streamlit as st
import boto3
import json

# AWS config - replace with your details
AWS_REGION = "ap-south-1"  # Change if different
SAGEMAKER_ENDPOINT = "spam-ham-endpoint"  # Your SageMaker endpoint name

# Connect to AWS SageMaker
runtime = boto3.client("sagemaker-runtime", region_name=AWS_REGION)

def predict_email(email_text):
    # Send the email text to SageMaker endpoint
    response = runtime.invoke_endpoint(
        EndpointName=SAGEMAKER_ENDPOINT,
        ContentType="application/json",
        Body=json.dumps({"text": email_text})
    )
    
    # Decode the response
    result = json.loads(response["Body"].read().decode())
    return result.get("prediction", "Unknown")

# Streamlit UI
st.set_page_config(page_title="AWS Spam vs Ham Classifier", page_icon="📧", layout="centered")

st.title("📧 AWS Spam vs Ham Classifier")
st.write("Enter your email content below to check if it’s spam or ham using your AWS ML model.")

email_input = st.text_area("Email Content", height=200)

if st.button("Check"):
    if email_input.strip() == "":
        st.warning("Please enter some email text first.")
    else:
        try:
            prediction = predict_email(email_input)
            if prediction.lower() == "spam":
                st.error("🚨 Spam Email Detected!")
            elif prediction.lower() == "ham":
                st.success("✅ This looks like Ham (Not Spam)")
            else:
                st.warning(f"Prediction: {prediction}")
        except Exception as e:
            st.error(f"Error connecting to AWS: {e}")