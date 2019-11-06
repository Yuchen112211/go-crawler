package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

func crawl(url string) string {
	var client http.Client

	response, err := client.Get(url)

	if err != nil {
		log.Fatal(err)
	}

	if response.StatusCode == http.StatusOK {
		bodyBytes, err :=  ioutil.ReadAll(response.Body)
		if err != nil {
			log.Fatal(err)
		}
		bodyString := string(bodyBytes)
		return bodyString
	}

	return "Something went wrong."
}


func main() {
	var res string
	res = crawl("http://127.0.0.1:8000/polls/")
	fmt.Println(res)
}
