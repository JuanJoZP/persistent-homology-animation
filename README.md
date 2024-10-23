# Instalation
```
conda create -n my_venv numpy pip 
conda activate my_venv
conda install -c conda-forge manim
pip install "manim-slides[pyqt6]"
```
- Generate video for each scene with `manim scene.py`
- Present slides with `manim-slides scene1 scene2 ...`
