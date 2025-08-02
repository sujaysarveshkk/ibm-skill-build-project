import requests

url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/chat?version=2023-05-29"

body = {
	"messages": [{"role":"user","content":[{"type":"text","text":"Act like an AI course advisor. I am a student who is a beginner in both Artificial Intelligence and Cybersecurity. Suggest a personalized 6-month learning roadmap that can help me become job-ready. Include key topics, tools, certifications, and suggested platforms for each month."}]},{"role":"assistant","content":"6-Month Learning Roadmap for Beginners in AI and Cybersecurity:\n\n**Month 1-2: Foundations of AI and Cybersecurity**\n\n*Topics:*\n- Introduction to AI: History, types, and applications\n- Basic programming concepts (Python)\n- Introduction to Cybersecurity: Principles, threats, and vulnerabilities\n\n*Tools:*\n- Python (Jupyter Notebook)\n- Virtual machines (VirtualBox or VMware)\n\n*Platforms:*\n- Coursera: \"AI For Everyone\" by Andrew Ng, \"Python for Everybody\" by University of Michigan\n- Udemy: \"Complete Cyber Security Course: Become a Cyber Security Expert\"\n- Khan Academy: Introduction to Computer Programming\n\n*Certifications:*\n- CompTIA IT Fundamentals (ITF+)\n\n**Month 3-4: Intermediate AI and Cybersecurity**\n\n*Topics:*\n- Machine Learning Basics (Supervised, Unsupervised, and Reinforcement Learning)\n- Deep Learning (Neural Networks, CNN, RNN)\n- Ethical Hacking and Penetration Testing\n- Cryptography\n\n*Tools:*\n- TensorFlow/Keras, PyTorch (for Deep Learning)\n- Metasploit, Wireshark, Nmap (for Ethical Hacking)\n\n*Platforms:*\n- Coursera: \"Machine Learning\" by Andrew Ng, \"Deep Learning Specialization\" by deeplearning.ai\n- Cybrary: \"Introduction to Ethical Hacking\"\n- Pluralsight: \"Cryptography for Hackers\"\n\n*Certifications:*\n- CompTIA Security+\n- Certified Ethical Hacker (CEH)\n\n**Month 5: Specialization in AI or Cybersecurity**\n\n*Topics:*\n- Choose one domain to specialize in:\n  - AI: Natural Language Processing (NLP), Computer Vision, or Robotics\n  - Cybersecurity: Incident Response, Risk Management, or Compliance\n\n*Tools & Platforms:*\n- Continue with tools and platforms from the previous months, focusing on your chosen specialization.\n\n*Certifications:*\n- Microsoft Certified: Azure AI Engineer Associate\n- Offensive Security Certified Professional (OSCP)\n\n**Month 6: Project Work and Portfolio Building**\n\n*Topics:*\n- Work on personal projects or participate in Kaggle competitions (AI)\n- Capture the Flag (CTF) competitions or bug bounty programs (Cybersecurity)\n\n*Tools & Platforms:*\n- GitHub for version control and project hosting\n- Kaggle for AI competitions\n- TryHackMe, Hack The Box, or VulnHub for CTF and bug bounty practice\n\n*Certifications:*\n- No formal certifications, but focus on building a strong portfolio showcasing your skills and projects.\n\nThroughout the 6 months, dedicate time to practice coding, participate in online communities (e.g., Stack Overflow, Reddit), and network with professionals in the field. Regularly update your knowledge by following relevant blogs, podcasts, and newsletters. Good luck on your learning journey!"}],
	"project_id": "ee06b7cb-a91c-4b7b-8f22-4a82d970854c",
	"model_id": "ibm/granite-3-3-8b-instruct",
	"frequency_penalty": 0,
	"max_tokens": 2000,
	"presence_penalty": 0,
	"temperature": 0,
	"top_p": 1
}

headers = {
	"Accept": "application/json",
	"Content-Type": "application/json",
	"Authorization": "Bearer YOUR_ACCESS_TOKEN"
}

response = requests.post(
	url,
	headers=headers,
	json=body
)

if response.status_code != 200:
	raise Exception("Non-200 response: " + str(response.text))

data = response.json()
