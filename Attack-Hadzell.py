a
    s(
`  �                   @   s   d dl mZ d dlmZ d dlmZ zd dlmZ W n eyN   ed� Y n0 dZ	dd� Z
d	d
� Zedk�r�ed� e�  ed� e�  ed� e�  ed� e�  ed� e�  ed� ed� eee	d�� eedd�� eedd�� eedd�� eedd�� eedd�� eedd��Zdev �rNe
�  eede d�� �q6n�dev �rve
�  eede d�� �q^n�dev �r�e
�  eede d�� �q�n^dev �r�e
�  eede d�� �q�n6dev �r�e
�  eede d�� �q�need d!�� d"S )#�    )�stdout)�system)�sleep)�coloredzpip install termcolorzl
 _______         __  __
|   |   |.--.--.|  ||  |--.
|       ||  |  ||  ||    <
|___|___||_____||__||__|__|
c                  C   s`   d} d}t d�D ]J}td� ttd|� d| � d�d�d	d
d� |d7 }|dkrd}| d7 } qd S )N�#r   �e   皙�����?z	Loading z% [�]�green� T)�end�flush�   �   )�ranger   �printr   )�load�count�x� r   �hulk-Hadzell.py�loading   s    "r   c                 C   s(   | D ]}t �|� t ��  td� qd S )Nr   )r   �writer   r   )�kata�zr   r   r   �jalan   s    
r   �__main__z script ini untuk ddos sebuah webzddos lah untuk kebenaran okez!jangan ddos web yang berbagi ilmuz!makasih buat hazi dah nemenin guaz+sampe sekarang walaupun orang nya goblok :)r   �clear�redz==========================z Author  : HadsXdev       r
   z Contact : 085793378137   z Thanks  : HazellNut      u   [✓] target : �.zAttack to ip : �1�2�7�3zconnection time out�cyanN)�sysr   �osr   �timer   �	termcolorr   �ModuleNotFoundError�logor   r   �__name__r   �input�targetr   r   r   r   �<module>   sZ   






