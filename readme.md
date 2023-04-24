# SeleniumでWeb情報を取得

## Teams Web版のページを開いてユーザとパスワード自動入力する

### Python環境設定

* Python 3.xのインストール
  * [Python環境構築ガイド](https://www.python.jp/install/install.html)
* Pythonのバーチャル環境作成と有効化
  * [Pythonのvenvの使い方（基礎編）をご紹介](https://rainbow-engine.com/python-venv-howto/)

### スクリプトの基本設定

* Pythonバーチャル環境が**有効化**されている状態で、下記のライブラリーをpipでインストールする

```bash
pip install --upgrade pip
pip install python-dotenv selenium
```

* Chromeドライバーの設定
  * ChromeドライバーはインストールされているChromeブラウザのバージョンによって異なるため、下記のサイトで手順を参考にしてドライバをダウンロードしてください
    * [Chrome Driverのインストール方法](https://zenn.dev/ryo427/articles/7ff77a86a2d86a)
  * ダウンロードしたexeファイルを./drv/の配下に配置しておきます

### スクリプトソース解読

```python
usernameStr = "Teamsのユーザ名"
passwordStr = "Teamsのログインパスワード"
browser = webdriver.Chrome(
    executable_path="./drv/chromedriver" # Chromeドライバーのパスを定義する
)
browser.get(
    'https://login.microsoftonline.com/common/xxxxxxx'
)　# 最初に開きたいページのURLをここで定義する（本例ではTeams Web版のログインページ）
```

```python
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located(
        (By.ID, 'i0116') # idがi0116のElement（Email入力欄）が表示されるまで待つ
    )
)
```

```python
username = browser.find_element(By.ID, 'i0116')  # idでElement（Email入力欄）を検索
username.send_keys(usernameStr)  # Elementに値をセット
browser.find_element(By.ID, 'idSIButton9').click()  # 「次へ」ボタンをIDで検索して押下の動作をする
```

```python
msgContent = browser.find_elements(By.XPATH, '//*[@data-tid="messageBodyContent"]/div')  # XPATHでMessageカード一覧を取得（パターンに該当するElementが対象）
for msgTxt in msgContent:
    print(msgTxt.get_attribute('innerText'))  # 各Messageカードの文言を取得し、表示する

```

### 参考となったサイト

* [SeleniumLibrary](http://robotframework.org/SeleniumLibrary/SeleniumLibrary.html)
* [図解】XPathとは？基本概念から書き方までわかりやすく解説！](https://www.octoparse.jp/blog/xpath-introduction/)
* [ChromeでXPathを取る・検証する](https://qiita.com/ywindish/items/5a992c49387d81df900e)