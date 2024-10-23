# Instalation
```
conda create -n my_venv manim numpy pip
conda activate my_venv
pip install manim-slides[pyqt6, manim]
```
- Generate video for each scene with `manim scene.py`
- Present slides with `manim-slides scene1 scene2 ...`
