/*
 Design a data structure that simulates an in-memory file system.
 
 Implement the FileSystem class:
 
 FileSystem() Initializes the object of the system.
 List<String> ls(String path)
 If path is a file path, returns a list that only contains this file's name.
 If path is a directory path, returns the list of file and directory names in this directory.
 The answer should in lexicographic order.
 void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
 void addContentToFile(String filePath, String content)
 If filePath does not exist, creates that file containing given content.
 If filePath already exists, appends the given content to original content.
 String readContentFromFile(String filePath) Returns the content in the file at filePath.
 */

import Foundation

// sc: O(mn)
// m: how many vertical lines
// n: average length of path
class FileSystem {
    var root: FileNode!
    
    init() {
        root = FileNode()
        root.content = "/"
    }
    
    // tc: O(m+klogk)
    // m: path length
    // k: sort last layers files
    func ls(_ path: String) -> [String] {
        var currentNode: FileNode = root
        var files: [String] = []
        
        if path != root.content {
            let folders: [String] = path.components(separatedBy: "/")
            for i in 0..<folders.count {
                if let file = currentNode.files[folders[i]] {
                    currentNode = file
                }
            }
            if currentNode.isFile, let last = folders.last {
                files.append(last)
                return files
            }
        }
        
        return currentNode.files.keys.sorted()
    }
    
    // tc: O(m)
    // m: length of path
    func mkdir(_ path: String) {
        var temp: FileNode? = root
        let folders = path.split(separator: "/")
        
        for i in 0..<folders.count {
            if temp?.files[String(folders[i])] == nil {
                temp?.files[String(folders[i])] = FileNode()
            }
            temp = temp?.files[String(folders[i])]
        }
    }
    
    // tc: O(m)
    // m: length of path
    func addContentToFile(_ filePath: String, _ content: String) {
        var temp: FileNode? = root
        let folders = filePath.split(separator: "/")
        
        for i in 0..<folders.count - 1 {
            temp = temp?.files[String(folders[i])]
        }
        if temp?.files[String(folders[folders.count - 1])] == nil {
            temp?.files[String(folders[folders.count - 1])] = FileNode()
        }
        
        temp = temp?.files[String(folders[folders.count - 1])]
        temp?.isFile = true
        temp?.content = temp!.content + content
    }
    
    // tc: O(m)
    // m: length of path
    func readContentFromFile(_ filePath: String) -> String {
        var temp: FileNode = root
        let folders = filePath.split(separator: "/")
        
        for i in 0..<(folders.count - 1) {
            if let file = temp.files[String(folders[i])] {
                temp = file
            }
        }
        if let last = folders.last, let file: FileNode = temp.files[String(last)] {
            return file.content
        }
        return ""
    }
}

class FileNode {
    var isFile = false
    var files: [String: FileNode] = [String: FileNode]()
    var content = ""
}
