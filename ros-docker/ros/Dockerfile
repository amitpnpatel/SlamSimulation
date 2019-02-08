FROM osrf/ros:melodic-desktop-full-bionic
#RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
RUN apt-get update && apt-get install -y \
    tmux \
    zsh \
    curl \
    wget \
    vim \
    sudo \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    mesa-utils \
    unzip openssh-server xauth\
    && rm -rf /var/likb/apt/lists/*
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
#RUN curl -sSL http://get.gazebosim.org | sh
#CMD ["rosrun", "gazebo_ros gazebo"]
CMD ["./entrypoint.sh"]
#ENTRYPOINT ["/entrypoint.sh"]
