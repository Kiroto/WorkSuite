
"Hello World!\n" print

System args foreach(i, arg, write("'", i, "' = ", arg, "\n"))

k := System getEnvironmentVariable("JAVA_HOME")

write(k, "\n")

file := File openForUpdating("./Hello.txt")
file write("sambacutiricutamba\nlabatiracatitumba\nabcdefg")
file rewind
file readLines foreach(i, line, write("'Line ", i, "' = ", line, "\n"))
file close

Curses begin

data := Curses get(5)

data println

// nombre := Socket URL with("https://example.com")
