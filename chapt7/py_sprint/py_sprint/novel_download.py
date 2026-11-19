import threading #
import requests

class Download:
    def download(self,url,callback_word_count):
        print(f"{threading.get_ident()}开始下载{url}")
        response = requests.get(url) #向指定的 url 发送 HTTP GET 请求，获取服务器响应
        response.encoding = 'UTF-8' #告诉 requests 用 UTF-8 编码来解码响应内容（因为服务器返回的内容是字节，需要转换成字符串）。设置编码后，访问 response.text 时就会把字节流按 UTF-8 解码成字符串。
        callback_word_count(url,response.text) #把下载的url和下载内容返回给下面def word_count(url,result)函数，并且运行这个函数，因为现在callback_word_count就代表def word_count(url,result)这个函数

    def start_download(self,url,callback_word_count):
        thread = threading.Thread(target=self.download,args=(url,callback_word_count)) #创建了一个新的线程对象 thread，这个线程执行时会调用 self.download 方法，且给它传递两个参数 url 和 callback_word_count。
        thread.start()

def word_count(url,result):
    print(f"{url}:{len(result)}->{result[:5]}") #打印输出url和长度，以及0到5的内容

def main():
    download_node = Download()
    download_node.start_download("http://0.0.0.0:8000/src/py_sprint/novel.txt",word_count) #最主要的函数，把def word_count(url,result)：给callback_word_count这个，他俩就是一体的了。运行这个callback_word_count就是运行这个函数。
