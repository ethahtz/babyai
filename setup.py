from setuptools import setup

setup(
    name='babyai',
    version='1.1',
    license='BSD 3-clause',
    keywords='memory, environment, agent, rl, openaigym, openai-gym, gym',
    packages=['babyai', 'babyai.levels', 'babyai.utils'],
    install_requires=[
        'gym==0.17.2',
        'numpy==1.15.4', # Temporary: fix numpy version because of bug introduced in 1.16
        "torch>=0.4.1",
        'blosc>=1.5.1',
        'gym_minigrid==1.0.1',
    ],
)
