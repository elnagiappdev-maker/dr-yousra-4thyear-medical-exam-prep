# Deployment Guide

This guide covers multiple deployment options for the Medical Exam Prep Streamlit application.

## Table of Contents
1. [Local Development](#local-development)
2. [Streamlit Cloud](#streamlit-cloud)
3. [Docker Deployment](#docker-deployment)
4. [Heroku Deployment](#heroku-deployment)
5. [AWS Deployment](#aws-deployment)
6. [Self-Hosted Server](#self-hosted-server)

---

## Local Development

### Prerequisites
- Python 3.8+
- Git
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/med_exam_prep_streamlit.git
cd med_exam_prep_streamlit
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run app.py
```

5. Access the app:
```
http://localhost:8501
```

---

## Streamlit Cloud

### Recommended for Quick Deployment

Streamlit Cloud is the easiest way to deploy your app for free.

### Steps

1. **Push to GitHub**
   - Create a GitHub repository
   - Push your code:
   ```bash
   git remote add origin https://github.com/yourusername/med_exam_prep_streamlit.git
   git branch -M main
   git push -u origin main
   ```

2. **Connect to Streamlit Cloud**
   - Go to [Streamlit Cloud](https://streamlit.io/cloud)
   - Click "New app"
   - Select your GitHub repository
   - Choose the branch (main)
   - Set main file path to `app.py`
   - Click "Deploy"

3. **Your app will be live at**
   ```
   https://<username>-med-exam-prep-streamlit-<branch>.streamlit.app
   ```

### Configuration
- Streamlit Cloud automatically reads from `.streamlit/config.toml`
- Set environment variables in the app settings if needed

---

## Docker Deployment

### Prerequisites
- Docker
- Docker Compose (optional)

### Using Docker Compose (Recommended)

1. Build and run:
```bash
docker-compose up --build
```

2. Access the app:
```
http://localhost:8501
```

### Using Docker Directly

1. Build the image:
```bash
docker build -t med-exam-prep-streamlit .
```

2. Run the container:
```bash
docker run -p 8501:8501 med-exam-prep-streamlit
```

3. Access the app:
```
http://localhost:8501
```

### Docker Hub (Optional)

1. Tag your image:
```bash
docker tag med-exam-prep-streamlit yourusername/med-exam-prep-streamlit:latest
```

2. Push to Docker Hub:
```bash
docker login
docker push yourusername/med-exam-prep-streamlit:latest
```

---

## Heroku Deployment

### Prerequisites
- Heroku account
- Heroku CLI installed
- Git

### Steps

1. **Create Heroku app**
```bash
heroku login
heroku create your-app-name
```

2. **Create Procfile**
```bash
echo "web: streamlit run app.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile
```

3. **Deploy**
```bash
git push heroku main
```

4. **View logs**
```bash
heroku logs --tail
```

5. **Access your app**
```
https://your-app-name.herokuapp.com
```

---

## AWS Deployment

### Option 1: AWS EC2

1. **Launch EC2 Instance**
   - AMI: Ubuntu 22.04 LTS
   - Instance type: t2.micro (free tier)
   - Security group: Allow port 8501

2. **Connect and setup**
```bash
ssh -i your-key.pem ubuntu@your-instance-ip

# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install -y python3-pip python3-venv

# Clone repository
git clone https://github.com/yourusername/med_exam_prep_streamlit.git
cd med_exam_prep_streamlit

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Streamlit
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
```

3. **Access your app**
```
http://your-instance-ip:8501
```

### Option 2: AWS AppRunner

1. Create a Docker image and push to ECR
2. Create AppRunner service
3. Connect to your ECR repository
4. Deploy

---

## Self-Hosted Server

### Using Nginx as Reverse Proxy

1. **Install dependencies**
```bash
sudo apt update
sudo apt install -y python3-pip python3-venv nginx supervisor
```

2. **Setup application**
```bash
cd /var/www
git clone https://github.com/yourusername/med_exam_prep_streamlit.git
cd med_exam_prep_streamlit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. **Create Supervisor config** (`/etc/supervisor/conf.d/streamlit.conf`)
```ini
[program:streamlit]
directory=/var/www/med_exam_prep_streamlit
command=/var/www/med_exam_prep_streamlit/venv/bin/streamlit run app.py --server.port=8501 --server.address=127.0.0.1
user=www-data
autostart=true
autorestart=true
stderr_logfile=/var/log/streamlit.err.log
stdout_logfile=/var/log/streamlit.out.log
```

4. **Update Supervisor**
```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start streamlit
```

5. **Configure Nginx** (`/etc/nginx/sites-available/default`)
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

6. **Enable and restart Nginx**
```bash
sudo systemctl enable nginx
sudo systemctl restart nginx
```

---

## SSL/HTTPS Setup

### Using Let's Encrypt with Certbot

```bash
sudo apt install -y certbot python3-certbot-nginx

# Get certificate
sudo certbot --nginx -d your-domain.com

# Auto-renewal
sudo systemctl enable certbot.timer
sudo systemctl start certbot.timer
```

---

## Performance Optimization

### Caching
- Use `@st.cache_data` for expensive computations
- Cache the questions database loading

### Database
- Consider migrating to a database for production
- Add user authentication for progress tracking

### CDN
- Use CloudFlare for static content delivery
- Improves load times globally

---

## Monitoring and Maintenance

### Logs
- Monitor application logs regularly
- Set up log aggregation (e.g., ELK stack)

### Uptime Monitoring
- Use services like UptimeRobot
- Set up alerts for downtime

### Backups
- Regular backups of questions database
- Version control for code

### Updates
- Keep dependencies updated
- Monitor security advisories

---

## Troubleshooting

### Port Already in Use
```bash
# Find process using port 8501
lsof -i :8501

# Kill process
kill -9 <PID>
```

### Memory Issues
```bash
# Increase available memory
# For Docker: docker run -m 2g ...
# For Heroku: heroku dyno:resize standard-2x
```

### SSL Certificate Issues
```bash
# Renew certificate manually
sudo certbot renew --force-renewal
```

---

## Cost Estimation

| Platform | Cost | Best For |
|----------|------|----------|
| Streamlit Cloud | Free | Development, small projects |
| Heroku | $7-50/month | Small to medium apps |
| AWS EC2 | $5-30/month | Scalable applications |
| Self-hosted | $5-20/month | Full control |
| DigitalOcean | $5-40/month | Simplicity |

---

## Support

For deployment issues, refer to:
- [Streamlit Documentation](https://docs.streamlit.io)
- [Docker Documentation](https://docs.docker.com)
- [Heroku Documentation](https://devcenter.heroku.com)
- [AWS Documentation](https://docs.aws.amazon.com)

---

**Last Updated**: October 2025
