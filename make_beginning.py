import os
import shutil as sh

if os.path.exists('neuer_ordner'):
    sh.rmtree('neuer_ordner')  # Löscht den Ordner, falls er bereits existiert
os.mkdir('neuer_ordner')
os.chdir('neuer_ordner')
for i in range(1, 200):
    os.mkdir(f'neuer_ordner{i}')
    os.chdir(f'./neuer_ordner{i}')
    file = open('Think.txt', 'a')
    file.write('LernOS ist ein Lernsystem, das auf dem Konzept des lebenslangen Lernens basiert.\n')
    file.write('Es fördert die Selbstorganisation und die individuelle Gestaltung des Lernprozesses.\n')
    file.close()
    os.chdir('./..')

print("Ordner und Dateien wurden erfolgreich erstellt.")
