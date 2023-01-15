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
