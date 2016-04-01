import sys
import editor

cont = editor.edit(contents='ABC!',
                   use_tty='use_tty' in sys.argv)
sys.stdout.write(cont)
