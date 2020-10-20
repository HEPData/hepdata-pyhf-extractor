PACKAGE_VERSION = $(shell cat VERSION)
COV_CONFIG = ".coveragerc"
SOURCE_FOLDER = "src"
TESTS_FOLDER = "tests"
TESTS_PARAMS = "-p no:cacheprovider"


.PHONY: check
check:
	@echo "Checking code format"
	@black --check $(SOURCE_FOLDER)
	@black --check $(TESTS_FOLDER)


tag-%:
	@echo "Bumping and tagging version"
	@$(eval PART := $*)
	@bump2version --current-version $(PACKAGE_VERSION) $(PART)


.PHONY: test
test:
	@echo "Testing code"
	@pytest --cov-config=$(COV_CONFIG) --cov=$(SOURCE_FOLDER) "$(TESTS_PARAMS)"
