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


.PHONY: tag
tag:
	@echo "Tagging current version"
	@git tag --annotate "v$(PACKAGE_VERSION)" --message "Tag v$(PACKAGE_VERSION)"
	@git push --follow-tags


.PHONY: test
test:
	@echo "Testing code"
	@pytest --cov-config=$(COV_CONFIG) --cov=$(SOURCE_FOLDER) "$(TESTS_PARAMS)"
