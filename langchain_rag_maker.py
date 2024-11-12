from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
import os
import tkinter as tk
from tkinter import filedialog

class LangchainRagMaker:
    # 해당 디렉토리의 모든 파일명을 가져오는 함수
    def _get_all_files_in_directory(self, dir):
        # 해당 디렉토리의 모든 파일 리스트 가져오기
        files = [os.path.join(dir, file) for file in os.listdir(dir)]
        return files

    def load(self):
        result = []

        # 파일 선택 창을 띄워서 파일을 선택한다. 이 때 엑셀 파일로 한정한다.
        # root = tk.Tk()
        # root.withdraw()
        # folder_path = filedialog.askdirectory(initialdir="./")
        folder_path = "./rag_documents"

        # 폴더 내의 모든 텍스트 파일을 불러와 RAG 문서화 한다.
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size = 300,
            chunk_overlap = 50,
            length_function = len
        )
        file_paths = self._get_all_files_in_directory(folder_path)
        for file_path in file_paths:
            data = TextLoader(file_path, encoding="utf-8").load()
            texts = text_splitter.split_text(data[0].page_content)
            result.append(data)
        return result