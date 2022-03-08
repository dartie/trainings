---
title:
- Go Advanced
author:
- Dario Necco
theme:
- Nalug
date:
- Dec 11, 2021
---

---#
![](Go-advanced-Nalug/golang-teacher.png)

---#

# reveal-deck changes
[revealjs Project](https://revealjs.com/)
<br>
[reveal-deck Repo](https://gitlab.com/dartie/reveal-deck)

<br>
<br>

## Support for code line numbers

```
{data-line-numbers="all|11|all"}
{data-line-numbers="all|11|all"}
```

```
{data-line-numbers="1,4|all"}
{data-line-numbers="1,4|all"}
```

```
{data-line-numbers="1-2|all"}
{data-line-numbers="1-2|all"}
```

<br>
<br>

```c++
{data-line-numbers="all|2|all"}
int main() {
  return 0;
}
```

---##
## Support for markdown tables

| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |

---##
## Support for emoji

* List here: [iemoji.com](https://www.iemoji.com/emoji-cheat-sheet/all)

:heart:
:desert:

---##
## Toolbar for overview 
## (Table Of Content)

---##
## Slide overview
`ESC` button

---##
## Copy button for snippet 

```python
import os

print('Click on "Copy" for copying the this snippet to the clipboard')
```


---##
## Support for admonitions

* Supported syntax : [Mkdocs Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)

```
!!! note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
```

```
!!! danger

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
```

---##
!!! note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.


!!! summary

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.


!!! info

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.


!!! tip

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

---##

!!! success

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.


!!! help

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.


!!! warning

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

---##

!!! failure

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.


!!! danger

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.


!!! error

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.


!!! bug

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

---##

!!! example

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.


!!! quote

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

----------------------------------------------------------------------------------------------------------


---#
# Go Recap

---##
# Project structure

```bash
bin/
    myapp                    # Executable binary
    hello                    # Executable binary
pkg/
   github.com/gorilla/
       mux.a                 # Package archive
   go.uber.org/
       zap.a                 # Package archive
src/
    hello/                   # Local package (not published)
       hello.go
       foo/
          foo.go
```

!!! note

    `foo` sub-package can be imported from `hello.go` using `import "hello/foo"`


!!! warning

    Only functions/variables declared in the sub-package with Title case can be used in `hello.go`


---##
# Project initialization

```bash
# from src folder
mkdir app
cd app
go mod init  # creates go.mod which contains dependencies

nano app.go
```

---##
# Write your .go code

```go
{data-line-numbers="1|3|4|6|11|14|16|18|all"}
package main // package name

import "fmt"              // built-in package import
import "rsc.io/quote"     // 3-party package import ("go get rsc.io/quote")

var slice = []string{ // variable declared with "var"
	"stringElement1",
	"stringElement2",
}

func main() { // main function: package entry-point
  fmt.Println(quote.Go())

	years := 4 // variable initialized with := (type is automatically detected)

	fmt.Printf("John is %d years old\n", years)

	for _, f := range slice {  // for loop
		fmt.Println(">", f)
	}
}

/* Things to remember
1. Unused variables are not allowed
2. Unused imported packages are not allowed
*/
```

---##

```go
/* Things to remember
1. Unused variables are not allowed
2. Unused imported packages are not allowed
*/
```

---##
# Compilation

```bash
go tidy  # downloads dependencies (rsc.io/quote)
go build
```

* Target platform and architecture are determined respectively by `$GOOS` and `$GOARCH` environment variables

```bash
GOOS=linux GOARCH=amd64 go build -o bin/app-amd64-linux app.go
```

* The valid combinations of `$GOOS` and `$GOARCH` are [here](https://go.dev/doc/install/source#environment)


---##
# Run the app

```bash
./app
```

----------------------------------------------------------------------------------------------------------

---#
# init() function

* Runs before any other function (even before `main()`)
* Used for: 
    * Creating connections to databases
    * Loading in configuration from local configuration files

```go
package main

func init() {
  fmt.Println("This will get called on main initialization")
}

func main() {
  fmt.Println("My Wonderful Go Program")
}
```

```
$ go run test.go
This will get called on main initialization
My Wonderful Go Program
```

---##
## Order of functions execution

```go
package main

import "fmt"

var Variable = foo()

func init() {
    fmt.Println("init() has run")
}

func foo() int {
    fmt.Println("foo() has run")
    return 43
}

func main() {
    fmt.Println("main() has run")

    fmt.Println(Variable)
}
```

---##
```
foo() has run
init() has run
main() has run.
43
```

---##
### Multiple Init Functions in the Same File

* Multiple init() functions are allowed
* These are called in their respective order of declaration within the file

```go
package main

import "fmt"

func init() {
    fmt.Println("init() 1")
}

func init() {
    fmt.Println("init() 2")
}

func main() {
    fmt.Println("main()")
}
```


---##
```
init() 1
init() 2
main()
```

---##
## To wrap up

* `foo()` is guaranteed to run before `init()` is called, and `init()` is guaranteed to run before `main()` is called.

* Keep in mind that `init()` is always called, regardless whether there is main or not, so if you import a package that has an init function, it will be executed.

* Additionally, you can have multiple `init()` functions per package; they will be executed in the order they show up in the file (after all variables are initialized of course). 

* If they span multiple files, they will be executed in lexical file name order


---##
![](Go-advanced-Nalug/init.png)

* If a package imports other packages, the latter are initialized first.

* Current package's constant initialized then.
 
* Current package's variables are initialized then.
 
* Finally, `init()` function of current package is called.

----------------------------------------------------------------------------------------------------------

---#
# Flags 

* Pass value to variables at linker time

```bash
go build -ldflags "-X main.version=3.0"
```

```go
package main

import "fmt"

var version string

func main() {
    fmt.Println(version)  // "" is printed if ldflags is not used
}
```

----------------------------------------------------------------------------------------------------------

---#
# Build Tags

* Identifier added to a piece of code that determines when the file should be included in a package during the build process. 
* This allows you to build different versions of your Go application from the same source code and to toggle between them in a fast and organized manner.

---##
Example: handle Free, Pro and Enterprise level of your application:

#### `main.go`
```go
package main

import "fmt"

var features = []string{
  "Free Feature #1",
  "Free Feature #2",
}

func main() {
  for _, f := range features {
    fmt.Println(">", f)
  }
}
```

---##
Build and run the program:
```bash
go build
./app
```

Output:
```
> Free Feature #1
> Free Feature #2
```

---##
#### `pro.go`

```go
package main

func init() {
  features = append(features,
    "Pro Feature #1",
    "Pro Feature #2",
  )
}
```

#### `main.go`
```go
package main

import "fmt"

var features = []string{
  "Free Feature #1",
  "Free Feature #2",
}

func main() {
  for _, f := range features {
    fmt.Println(">", f)
  }
}
```

---##

Build and run the program:
```bash
go build *.go
./app
```

```
> Free Feature #1
> Free Feature #2
> Pro Feature #1
> Pro Feature #2
```

* Undesired behaviour! 

---##
#### `pro.go`

```go
{data-line-numbers="1|all"}
//go:build pro

package main

func init() {
  features = append(features,
    "Pro Feature #1",
    "Pro Feature #2",
  )
}
```

Build and run the program:
```bash
go build -tags pro
./app
```

```
> Free Feature #1
> Free Feature #2
> Pro Feature #1
> Pro Feature #2
```

* pro has been included since `-tags pro` has been used.

---##
#### `enterprise.go`

```go
//go:build enterprise

package main

func init() {
	features = append(features,
		"Enterprise Feature #1",
		"Enterprise Feature #2",
	)
}
```

Build and run the program:
```bash
go build -tags enterprise
./app
```

```
> Free Feature #1
> Free Feature #2
> Enterprise Feature #1
> Enterprise Feature #2
> Pro Feature #1
> Pro Feature #2
```

---##
#### `enterprise.go`

```go
{data-line-numbers="1|all"}
//go:build pro && enterprise

package main

func init() {
	features = append(features,
		"Enterprise Feature #1",
		"Enterprise Feature #2",
	)
}
```


---##
Build and run the program:
```bash
go build -tags pro
./app
```

```
> Free Feature #1
> Free Feature #2
> Pro Feature #1
> Pro Feature #2
```

---##
Build and run the program:
```bash
go build -tags pro,enterprise
./app
```

```
> Free Feature #1
> Free Feature #2
> Enterprise Feature #1
> Enterprise Feature #2
> Pro Feature #1
> Pro Feature #2
```


---##
|      Build Tag Syntax      | Build Tag Sample               | Build Tag Sample (old syntax) | Boolean Statement      |
| :------------------------: | ------------------------------ | ----------------------------- | ---------------------- |
|  Space-separated elements  | `//go:build pro || enterprise` | `// +build pro enterprise`    | `pro` OR `enterprise`  |
|  Comma-separated elements  | `//go:build pro && enterprise` | `// +build pro,enterprise`    | `pro` AND `enterprise` |
| Exclamation point elements | `//go:build !pro`              | `// +build !pro`              | NOT `pro`              |


---##
# `//go:build` vs `// +build`

`//go:build` is the new conditional compilation directive introduced in Go 1.17.
It is meant to replace `// +build` directives, as the new syntax brings a few key improvements:

* Consistency with other existing Go directives and pragmas, e.g. `//go:generate`
* Support for standard boolean expression, e.g. `//go:build foo && bar`, whereas the old `// +build` comment has less intuitive syntax. For example `AND` was expressed with commas `// +build foo,bar` and `OR` with spaces `// +build foo bar`
* It's supported by `go fmt`, which will automatically fix incorrect placement of the directive in source files, thus avoiding common mistakes as not leaving a blank line between the directive and the package statement.

----------------------------------------------------------------------------------------------------------

---#
# Variadic functions

Variadic functions can be called with any number of trailing arguments. 

!!! example 

    `fmt.Println` is a common variadic function.


* If you already have multiple args in a slice, apply them to a variadic function using func(slice...) like this.

---##
```go
{data-line-numbers="5|16|17|20|all"}
package main

import "fmt"

func sum(nums ...int) {
    fmt.Print(nums, " ")
    total := 0
    for _, num := range nums {
        total += num
    }
    fmt.Println(total)
}

func main() {

    sum(1, 2)
    sum(1, 2, 3)

    nums := []int{1, 2, 3, 4}
    sum(nums...)
}
```

----------------------------------------------------------------------------------------------------------

---#

# Tests

* Allows to test files and functions in Go projects


* `person.go`

```go
package person

import "errors"

type Person struct {
	age int
}

func NewPerson(age int) (*Person, error) {
	if age < 1 {
		return nil, errors.New("A person is at least 1 years old")
	}

	return &Person{
		age: age,
	}, nil
}

func (p *Person) older(other *Person) bool {
	return p.age > other.age
}
```

---##

* `person_tests.go`

```go
package person

import (
	"testing"
)

func TestNewPersonPositiveAge(t *testing.T) {
	_, err := NewPerson(1)
	if err != nil {
		t.Errorf("Expected person, received %v", err)
	}
}

func TestNewPersonNegativeAge(t *testing.T) {
	p, err := NewPerson(-1)
	if err == nil {
		t.Errorf("Expected error, received %v", p)
	}
}

func TestOlderFirstOlderThanSecond(t *testing.T) {
	p1, _ := NewPerson(1)
	p2, _ := NewPerson(2)

	if p1.older(p2) {
		t.Errorf("Expected p1 with age %d to be younger than p2 with age %d", p1.age, p2.age)
	}
}

func TestOlderSecondOlderThanFirst(t *testing.T) {
	p1, _ := NewPerson(2)
	p2, _ := NewPerson(1)

	if !p1.older(p2) {
		t.Errorf("Expected p1 with age %d to be older than p2 with age %d", p1.age, p2.age)
	}
}
```

---##

```bash
$ go test person.go person_test.go
ok  	command-line-arguments	0.005s
```

!!! info

    Brief output since there are no errors


---##


## Options to run
<br>

### Test a specific test file
```bash
$ go test person.go person_test.go
ok  	command-line-arguments	0.005s
```

---##

### Test a go package
```bash
$ go test person
ok  	person	0.004s
```

---##

### Test a specific function
```bash
$ go test -run TestNewPerson -v
=== RUN   TestNewPersonPositiveAge
--- PASS: TestNewPersonPositiveAge (0.00s)
=== RUN   TestNewPersonNegativeAge
--- PASS: TestNewPersonNegativeAge (0.00s)
PASS
ok  	person	0.004s
```

---##
    
## Verbose flag `-v`

```bash
$ go test person.go person_test.go -v
=== RUN   TestNewPersonPositiveAge
--- PASS: TestNewPersonPositiveAge (0.00s)
=== RUN   TestNewPersonNegativeAge
--- PASS: TestNewPersonNegativeAge (0.00s)
=== RUN   TestOlderFirstOlderThanSecond
--- PASS: TestOlderFirstOlderThanSecond (0.00s)
=== RUN   TestOlderSecondOlderThanFirst
--- PASS: TestOlderSecondOlderThanFirst (0.00s)
PASS
ok  	command-line-arguments	0.005s
```

!!! info

    Verbose output with `-v` flag

---##

## Failing test `-failfast`

Cause a fail replacing `TestOlderFirstOlderThanSecond` function with 

```go
{data-line-numbers="all|5-7|all"}
func TestOlderFirstOlderThanSecond(t *testing.T) {
	p1, _ := NewPerson(100)
	p2, _ := NewPerson(2)

	if p1.older(p2) {
		t.Errorf("Expected p1 with age %d to be younger than p2 with age %d", p1.age, p2.age)
	}
}
```

---##

* `person_test.go`

```go
package person

import (
	"testing"
)

func TestNewPersonPositiveAge(t *testing.T) {
	_, err := NewPerson(1)
	if err != nil {
		t.Errorf("Expected person, received %v", err)
	}
}

func TestNewPersonNegativeAge(t *testing.T) {
	p, err := NewPerson(-1)
	if err == nil {
		t.Errorf("Expected error, received %v", p)
	}
}

func TestOlderFirstOlderThanSecond(t *testing.T) {
	p1, _ := NewPerson(100)
	p2, _ := NewPerson(2)

	if p1.older(p2) {
		t.Errorf("Expected p1 with age %d to be younger than p2 with age %d", p1.age, p2.age)
	}
}

func TestOlderSecondOlderThanFirst(t *testing.T) {
	p1, _ := NewPerson(2)
	p2, _ := NewPerson(1)

	if !p1.older(p2) {
		t.Errorf("Expected p1 with age %d to be older than p2 with age %d", p1.age, p2.age)
	}
}
```

---##

```bash
{data-line-numbers="all|6-7,11-13|all"}
$ go test -v
=== RUN   TestNewPersonPositiveAge
--- PASS: TestNewPersonPositiveAge (0.00s)
=== RUN   TestNewPersonNegativeAge
--- PASS: TestNewPersonNegativeAge (0.00s)
=== RUN   TestOlderFirstOlderThanSecond
--- FAIL: TestOlderFirstOlderThanSecond (0.00s)
    person_test.go:26: Expected p1 with age 100 to be younger than p2 with age 2
=== RUN   TestOlderSecondOlderThanFirst
--- PASS: TestOlderSecondOlderThanFirst (0.00s)
FAIL
exit status 1
FAIL	person	0.004s
```

`TestOlderFirstOlderThanSecond` is failed while others have passed.


---##


## Fast Failing

It allows to stop at the first fail

```bash
{data-line-numbers="all|1,7-11|all"}
$ go test -v -failfast
=== RUN   TestNewPersonPositiveAge
--- PASS: TestNewPersonPositiveAge (0.00s)
=== RUN   TestNewPersonNegativeAge
--- PASS: TestNewPersonNegativeAge (0.00s)
=== RUN   TestOlderFirstOlderThanSecond
--- FAIL: TestOlderFirstOlderThanSecond (0.00s)
    person_test.go:26: Expected p1 with age 100 to be younger than p2 with age 2
FAIL
exit status 1
FAIL	person	0.004s
```


----------------------------------------------------------------------------------------------------------

---#
# Coverage
<br>

Run the test and provide the coverage percentage
```bash
go test -cover
```

Sample output:

```
--- FAIL: TestOlderFirstOlderThanSecond (0.00s)
    person_test.go:26: Expected p1 with age 100 to be younger than p2 with age 2
FAIL
coverage: 100.0% of statements
exit status 1
FAIL	Go-Nalug/test-project	0.014s
```

---##

```bash
go test -v -coverprofile cover.out ./YOUR_CODE_FOLDER/...  # creates "cover.out"
go tool cover -html=cover.out -o cover.html
open cover.html
```

Creates a coverage html file which shows with colors what has been covered.

----------------------------------------------------------------------------------------------------------

---#
# Go doc

```go
//Package math provide mathematical functions
package math


//Sum two integers and returns a result
func Sum(x int, y int) int {
    return x + y
}
```

* Print plain text documentation to standard output

```bash
go doc
```

```
package math // import "Go-Nalug/doctest"

Package math provide mathematical functions

func Sum(x int, y int) int
```

---##

* Print full plain text documentation

```bash
go doc -all
```

```
package math // import "Go-Nalug/doctest"

Package math provide mathematical functions

FUNCTIONS

func Sum(x int, y int) int
    Sum two integers and returns a result
```


* Run a web server and presents the documentation as a web page

```bash
# install "godoc"
go get golang.org/x/tools/cmd/godoc
```

```bash
godoc -http=:6060  # or "godoc -http=127.0.0.1:6060"
```

----------------------------------------------------------------------------------------------------------

---#
# panic - defer - recover

* Allow to handle abnormal conditions in Go.

## panic

Terminates the program prematurely.

When a function encounters a panic:

1. Its execution is stopped
1. Any deferred functions are executed
1. The argument passed to the panic function will be printed when the program terminates.

---##

```go
{data-line-numbers="all|7,10|all|18|10|all"}
package main

import "fmt"

func fullName(firstName *string, lastName *string) {  
    if firstName == nil {
        panic("runtime error: first name cannot be nil")
    }
    if lastName == nil {
        panic("runtime error: last name cannot be nil")
    }
    fmt.Printf("%s %s\n", *firstName, *lastName)
    fmt.Println("returned normally from fullName")
}

func main() {  
    firstName := "Elon"
    fullName(&firstName, nil)
    fmt.Println("returned normally from main")
}
```

---##

```
panic: runtime error: last name cannot be nil

goroutine 1 [running]:  
main.fullName(0xc00006af58, 0x0)  
    /tmp/sandbox210590465/prog.go:12 +0x193
main.main()  
    /tmp/sandbox210590465/prog.go:20 +0x4d
```


---##

## defer

Functions to be executed before panic leads to the program termination

```go
{data-line-numbers="all|18|20|6|11|6|18|all"}
package main

import "fmt"

func fullName(firstName *string, lastName *string) {  
    defer fmt.Println("deferred call in fullName")
    if firstName == nil {
        panic("runtime error: first name cannot be nil")
    }
    if lastName == nil {
        panic("runtime error: last name cannot be nil")
    }
    fmt.Printf("%s %s\n", *firstName, *lastName)
    fmt.Println("returned normally from fullName")
}

func main() {  
    defer fmt.Println("deferred call in main")
    firstName := "Elon"
    fullName(&firstName, nil)
    fmt.Println("returned normally from main")
}
```

---##

```go
deferred call in fullName  
deferred call in main  
panic: runtime error: last name cannot be nil

goroutine 1 [running]:  
main.fullName(0xc00006af28, 0x0)  
    /tmp/sandbox451943841/prog.go:13 +0x23f
main.main()  
    /tmp/sandbox451943841/prog.go:22 +0xc6
```


---##
## recover

Allows to recover from a panic, raising the error, but avoiding the program to terminate

```go
{data-line-numbers="all|5-9|24|26|12|17|6|7|27|24|all"}
package main

import "fmt"

func recoverFullName() {  
    if r := recover(); r!= nil {
        fmt.Println("recovered from ", r)
    }
}

func fullName(firstName *string, lastName *string) {  
    defer recoverFullName()
    if firstName == nil {
        panic("runtime error: first name cannot be nil")
    }
    if lastName == nil {
        panic("runtime error: last name cannot be nil")
    }
    fmt.Printf("%s %s\n", *firstName, *lastName)
    fmt.Println("returned normally from fullName")
}

func main() {  
    defer fmt.Println("deferred call in main")
    firstName := "Elon"
    fullName(&firstName, nil)
    fmt.Println("returned normally from main")
}
```

---##

```
recovered from  runtime error: last name cannot be nil  
returned normally from main  
deferred call in main
```


----------------------------------------------------------------------------------------------------------

---#
# Web-development

* Many web-framework are available
* However, Go can accomplish this easily using built-in packages.

---##
## Run a server

```go
{data-line-numbers="5|9|all"}
package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.ListenAndServe(":8080", nil)
}
```

---##
## Handle a request

```go
{data-line-numbers="all|9|13-15|all"}
package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/index", Index)
	http.ListenAndServe(":8080", nil)
}

func Index(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Hello, World!")
}
```

---## 
## Render a template


### `main.go`
```go
{data-line-numbers="all|8|11|17-19|all"}
package main

import (
    "html/template"
    "net/http"
)

var tpl *template.Template

func main() {
    tpl, _ = tpl.ParseFiles("index1.html")

    http.HandleFunc("/", index)
    http.ListenAndServe(":8080", nil)
}

func index(w http.ResponseWriter, r *http.Request) {
    tpl.Execute(w, nil)
}
```

---##

### `index1.html`

```html
<!DOCTYPE html>
<html>
  <head>
    <title>index1.html Temp</title>
    <meta charset="UTF-8">
  </head>
  
  <body>
      <h1>Hello from index1.html</h1>    
  </body>
</html>
```

---##

## Render a template from folder

### `main.go`

```go
{data-line-numbers="all|11|all"}
package main

import (
	"html/template"
	"net/http"
)

var tpl *template.Template

func main() {
	tpl, _ = tpl.ParseGlob("templates/*.html")

	http.HandleFunc("/", indexHandler)
	http.HandleFunc("/about", aboutHandler)
	http.HandleFunc("/contact", contactHandler)
	http.HandleFunc("/login", loginHandler)
	http.ListenAndServe(":8080", nil)
}
```

---##

```go
func indexHandler(w http.ResponseWriter, r *http.Request) {
	tpl.ExecuteTemplate(w, "index.html", nil)
}

func aboutHandler(w http.ResponseWriter, r *http.Request) {
	tpl.ExecuteTemplate(w, "about.html", nil)
}

func contactHandler(w http.ResponseWriter, r *http.Request) {
	tpl.ExecuteTemplate(w, "contact.html", nil)
}

func loginHandler(w http.ResponseWriter, r *http.Request) {
	tpl.ExecuteTemplate(w, "login.html", nil)
}
```


---##
## Nested template 
## (include a template in another)

```go
package main

import (
	"html/template"
	"net/http"
)

var tpl *template.Template

func main() {
	tpl, _ = tpl.ParseGlob("templates/*.html")
	http.HandleFunc("/", indexHandler)
	http.ListenAndServe(":8080", nil)
}

func indexHandler(w http.ResponseWriter, r *http.Request) {
	tpl.ExecuteTemplate(w, "index.html", nil)
}
```

---##

* `index.html`

```html
{{template "Header"}}
<h1>Body</h1>
{{template "Footer"}}
```

* `header.html`

```html
{{define "Header"}}
    <h1>Header</h1>
{{end}}
```

* `footer.html`

```html
{{define "Footer"}}
    <h1>Footer</h1>
{{end}}
```

---##
## Render a template with variables

```go
package main

import (
	"fmt"
	"html/template"
	"net/http"
)

var tpl *template.Template
var name = "John"

func main() {
	tpl, _ = tpl.ParseGlob("templates/*.html")
	http.HandleFunc("/welcome", welcomeHandler)
	http.ListenAndServe(":8080", nil)
}

func welcomeHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Println("indexHandler running")
	tpl.ExecuteTemplate(w, "welcome.html", name)
}
```

---##
## Template syntax

* `{{/* a comment */}}` Defines a comment
* `{{.}}` Renders the root element
* `{{.Name}}` Renders the “Name”-field in a nested element
* `{{if .Done}} {{else}} {{end}}` Defines an if/else-Statement
* `{{range .List}} {{.}} {{end}}`  Loops over all “List” field and renders each using `{{.}}`

```html
        {{if .Member}}   
            <h1>Thank you for joining</h1>
        {{else}}
            <h1>Please signup to enjoy memborship benefits</h1>
        {{end}}
```

---##

### Check a specific value
Binary comparison operators defined as functions

* `eq` Returns the boolean truth of `arg1 == arg2`
* `ne` Returns the boolean truth of `arg1 != arg2`
* `lt` Returns the boolean truth of `arg1 < arg2`
* `le` Returns the boolean truth of `arg1 <= arg2`
* `gt` Returns the boolean truth of `arg1 > arg2`
* `ge` Returns the boolean truth of `arg1 >= arg2`

---##

```html
{data-line-numbers="all|3-5|7,9,11,13,21|all"}
        passed in value: {{.}}<br><br>
        
        eq .Language "English": {{eq .Language "English"}}<br>
        eq .Language "Mandarin": {{eq .Language "Mandarin"}}<br>
        eq .Language "Spanish": {{eq .Language "Spanish"}}<br><br>

        {{if eq .Language "English"}}
            <h1>Hello</h1>
        {{else if eq .Language "Mandarin"}}
            <h1>你好</h1>
        {{else if eq .Language "Spanish"}}
            <h1>Hola</h1>
        {{else}}
        <hi>
            <ul>
                <li>Hello</li>
                <li>你好</li>
                <li>Hola</li>
            </ul>
        </hi>
        {{end}}
```

---##

```html
<!-- This is a HTML comment-->
{{/* This is a Go template comment */}}
<h1>Welcome {{.}}!</h1>
```

---##

### Range (Iteration)

```go
{data-line-numbers="all|14,21|all"}
package main

import (
	"html/template"
	"net/http"
)

type GroceryList []string

var tpl *template.Template
var g GroceryList

func main() {
	g = GroceryList{"milk", "eggs", "green beans", "cheese", "flour", "sugar", "broccoli"}
	tpl, _ = tpl.ParseGlob("templates/*.html")
	http.HandleFunc("/list", listHandler)
	http.ListenAndServe(":8080", nil)
}

func listHandler(w http.ResponseWriter, r *http.Request) {
	tpl.ExecuteTemplate(w, "groceries.html", g)
}
```


---##

* Template

```html
{data-line-numbers="all|10-12|all"}
<!DOCTYPE html>
<html>
    <head>
        <title>Grocery List</title>
    <meta charset="UTF-8">
    </head>
    <body>
        <h3>Grocery List</h3>
        <ul>
            {{range .}}
                <li>{{.}}</li>
            {{end}}
        </ul>
    </body>
</html>
```


---##

* Alternatively

```html
{data-line-numbers="all|10-12|all"}
<!DOCTYPE html>
<html>
    <head>
        <title>Grocery List</title>
    <meta charset="UTF-8">
    </head>
    <body>
        <h3>Grocery List</h3>
        <ol>
            {{range $element := .}}
                <li>Element: {{$element}} Value:{{.}}</li>
            {{end}}
        </ol>
    </body>
</html>
```

---##

* With index

```html
{data-line-numbers="all|10-12|all"}
<!DOCTYPE html>
<html>
    <head>
        <title>Grocery List</title>
    <meta charset="UTF-8">
    </head>
    <body>
        <h3>Grocery List</h3>
        <ol>
            {{range $index, $element := .}}
                <li>Index: {{$index}} Element: {{$element}} Value:{{.}}</li>
            {{end}}
        </ol>
    </body>
</html>
```


----------------------------------------------------------------------------------------------------------


---#
# Additional resources

* [tutorialedge.net](https://tutorialedge.net/course/golang/)
* [bogotobogo.com](https://www.bogotobogo.com/GoLang/GoLang_HelloWorld.php)
* [dev.to](https://dev.to/t/go)
* [golangbot.com](https://golangbot.com/panic-and-recover/)
