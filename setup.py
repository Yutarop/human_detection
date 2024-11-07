from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'human_detection'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.xml')),
        (os.path.join('share', package_name, "rviz2"), glob('rviz2/*')),
        (os.path.join('share', package_name, "display_pcd"), glob('display_pcd/pcd_bag/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='katoyutaro1122@icloud.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pre_processing = human_detection.pre_processing:main'
        ],
    },
)
