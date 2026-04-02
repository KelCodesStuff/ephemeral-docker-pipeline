# Build the test image and run the ephemeral container
.PHONY: test
test:
	# Build the Docker image targeting the 'test' stage
	docker build --target test -t ephemeral-test-env .

	# Run the container, remove it automatically upon exit (--rm)
	docker run --rm ephemeral-test-env
