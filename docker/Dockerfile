FROM python:3.5

ENV POSTS_GIT_REPO "https://github.com/jradd/blogdata.git"
ENV POSTS_GIT_REPO_SECRET "4a23b1b45cdaef7ddb68828627c743574684deba"

RUN mkdir -p /www && \
    cd www && \
    git clone https://github.com/jradd/blog && \
    cd blog && \
    pip install -r Requirements.in && \
    cd app && \
    git clone $POSTS_GIT_REPO

ADD https://raw.githubusercontent.com/jradd/blog/master/docker/start_server.sh /www
CMD ["chmod","+x","/www/start_server.sh"]

EXPOSE 5000

CMD ["sh","/www/start_server.sh"]
