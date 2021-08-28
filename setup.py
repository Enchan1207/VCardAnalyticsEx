#
# pipが読んでライブラリの諸々を設定するためのファイル
#
import glob
import setuptools, os

# requirements.txtを読む
requires = []
if os.path.exists("requirements.txt"):
    with open("requirements.txt", "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in list(filter(lambda line: line.strip() != "", filter(lambda line: not line.strip().startswith("#"), lines)))]
        requires = lines

setuptools.setup(
    name="vcflib",
    version="0.1.0",
    license="MIT",
    description="vCard library",
    author="Enchan1207",
    url="https://github.com/Enchan1207/VCardAnalyticsEx",
    packages=setuptools.find_packages("src"),
    install_requires=requires,
    package_dir={"": "src"},
    py_modules=[os.path.splitext(os.path.basename(path))[0] for path in glob.glob('src/*.py')],
    include_package_data=True,
    zip_safe=False
)
