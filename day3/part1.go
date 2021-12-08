package main

import "os"
import "bufio"
import "fmt"
import "strconv"

func main(){
	// Read data from file
	var data []int
	
	data, err := readData("day3-data.txt")
	if err !=nil{
		fmt.Println(err)
	}
	
	


}

func readData(filename string) ([]int, error){
	file, err := os.Open(filename)
	if err != nil{
		return nil, err
	}
	defer file.Close()

	var data []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan(){
		int_line, err := strconv.Atoi(scanner.Text())
		if err !=nil{
			return nil, err
		}
		data = append(data, int_line)
	}

	return data, scanner.Err()
}