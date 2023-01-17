# Summary

### Hello World

`go run main.go`で実行。

```go
/*
実行ファイルを生成する場合は`main`にしなければならない
`main`以外だとライブラリとして利用すると判断され、
`go build`しても実行ファイルは生成されないし、
`func main`があるファイルを`go run`しても`package command-line-arguments is not a main package`
と表示されて実行されない
また、`package main`である場合、`func main`は定義しなければならない
*/
package main

import "fmt"

func main() {
    fmt.Println("Hello World")
}
```

### Go CLI

- `go build`
  - 実行ファイルを生成
- `go run`
  - その場で実行
- `go fmt`
  - ファイルをフォーマット
- `go install`
  - パッケージをコンパイルし、インストールする
- `go get`
  - パッケージのソースコードをダウンロードする
- `go test`
  - テストを実行

### 変数

```go
func main() {
  /*
  helloという名前の変数を定義。
  値から型を推測できるため、`var hello = "Hello"`
  のように省略して定義可能。
  また、`var`自体も省略可能で、`hello := "hello"`
  のように`:=`を使って定義可能。
  */
  var hello string = "Hello!"

  /*
  複数の変数を一度に定義もできる。
  値から型を推測できるため、型を省略可能。
  また、`var自体も省略可能。
  */
  var num1, num2 int = 1, 2

  /*
  以下のように定義もできる。
  */
  var (
    hello string = "Hello"
    str1, str2 = "str1", "str2"
  )
}
```

### 関数

```go
func greetings(name string) string {
  return "Hello " + name
}
```

### 配列

```go
/*
`[]`の中に要素数を入れることで、
固定サイズの配列を定義できる。
*/
var array [2]string = [2]string{"a", "b"}
```

### スライス

```go
/*
配列では`[]`に要素数を入れていたが、
何も指定しないことでスライスとして定義できる。
*/
var slice []string = []string{"a", "b"}
// slice[0:1] -> "a"
// slice[0:] -> "a", "b"
// slice[:1] -> "a"
// slice[:] -> "a", "b"

// 追加
slice = append(slice, "c")
```
