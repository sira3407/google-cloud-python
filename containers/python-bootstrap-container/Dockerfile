# Use a multi-stage docker build to limit production dependencies.
FROM python:3.11.4-buster

# Create a non-root user and group
RUN groupadd -r myapp && \
    useradd --no-log-init -r -g myapp myapp && \
    chown -R myapp:myapp /app && \
    chmod 755 /entrypoint.sh

# Set the working directory to /app
WORKDIR /app

# Install dependencies
RUN apt update && apt install -y jq && \
    pip install -r requirements.txt

# Copy the application code
COPY requirements.txt . 
COPY . .

# Set the ownership of the application directory to the non-root user
# Set the entrypoint to switch to the non-root user before running the application
RUN chown -R myapp:myapp /app && \
    chmod 755 /entrypoint.sh

# Set the entrypoint to switch to the non-root user before running the application
# Use a multi-stage docker build to limit production dependencies.
FROM python:3.11.4-buster

# Create a non-root user and group
RUN groupadd -r myapp && \
    useradd --no-log-init -r -g myapp myapp && \
    chown -R myapp:myapp /app && \
    chmod 755 /entrypoint.sh

# Set the working directory to /app
WORKDIR /app

# Install dependencies
RUN apt update && apt install -y jq && \
    pip install -r requirements.txt

# Copy the application code
COPY requirements.txt . 
COPY . .

# Set the ownership of the application directory to the non-root user
# Set the entrypoint to switch to the non-root user before running the application
RUN chown -R myapp:myapp /app && \
    chmod 755 /entrypoint.sh

# Set the entrypoint to switch to the non-root user before running the application
ENTRYPOINT [ "su", "-c", "/entrypoint.sh", "myapp" ]
CMD [ "/bin/bash" ]
CMD [ "/bin/bash" ]

# Set the default command to run if no command is specified
CMD [ "/bin/bash" ]


CMD [ "/bin/bash" ]
ENTRYPOINT [ "su", "-c", "/entrypoint.sh", "myapp" ]

CMD [ "/bin/bash" ]
ENTRYPOINT [ "su", "-c", "/entrypoint.sh", "myapp" ]
CMD [ "/bin/bash" ]
RUN chown -R myapp:myapp /app

# Set the entrypoint to switch to the non-root user before running the application
RUN chmod 755 /entrypoint.sh
ENTRYPOINT [ "su", "-c", "/entrypoint.sh", "myapp" ]
ENTRYPOINT [ "/bin/bash" ]
CMD [ "/entrypoint.sh" ]
