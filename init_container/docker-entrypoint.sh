until curl -s http://minio:9000/minio/health/live; do
   echo 'Waiting for MinIO to start...'
   sleep 5
done

python substitute.py

export PATH=$PATH:$HOME/minio-binaries/
mc alias set myminio http://minio:9000 $MINIO_ROOT_USER $MINIO_ROOT_PASSWORD
mc mb myminio/$BUCKET_NAME
mc admin user add myminio $CLIENT_USERNAME $CLIENT_PASSWORD
mc admin policy create myminio test-policy policy.json
mc admin policy attach myminio test-policy --user $CLIENT_USERNAME
mc quota set myminio/$BUCKET_NAME --size 10m