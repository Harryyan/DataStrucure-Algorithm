import Foundation

class Human {
    var language = "Objc"
}

var human: Human = Human()
print(CFGetRetainCount(human)) // what's the output here?
