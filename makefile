#
#
#

.PHONY: cleanup test_all test_part

cleanup:
	@yes|pip uninstall elecbreakutil
	@pip install .

# `tests/` 以下全テストファイルを走査
test_all:
	python3 -m unittest discover tests

# 引数で指定されたクラスをテスト
test_part:
	@if [ -n "${CLASS}" ]; then \
		python3 -m unittest tests.test_${CLASS}.test${CLASS}; \
	else \
		echo "please specify test case."; \
	fi
