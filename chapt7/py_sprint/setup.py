from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'py_sprint'

# 要装到 share/<包名>/ 下的目录（写你 src/py_sprint 里实际的目录名）
DATA_DIRS = ['launch', 'urdf', 'rviz', 'config', 'world']

SKIP_DIRS = {'__pycache__', '.git', '.vscode', '.pytest_cache'}


def collect(prefix, src_dir):
    """递归收集 src_dir，保留层级，返回 data_files 片段"""
    items = []
    if not os.path.isdir(src_dir):
        return items
    for root, dirs, files in os.walk(src_dir):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        rel = os.path.relpath(root, src_dir)
        target = prefix if rel == '.' else os.path.join(prefix, rel)
        if files:
            items.append((
                os.path.join('share', package_name, target),
                [os.path.join(root, f) for f in files],
            ))
    return items


data_files = [
    ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
]
for d in DATA_DIRS:
    data_files += collect(d, d)

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jitaihero',
    maintainer_email='18813577865@163.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            # "novel_download = py_sprint.novel_download:main",
        ],
    },
)

