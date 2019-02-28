FROM python:onbuild
ENV PORT 8080
EXPOSE 8080
ENV TEST 1234 
ENTRYPOINT ["python"]
CMD ["app.py"]
