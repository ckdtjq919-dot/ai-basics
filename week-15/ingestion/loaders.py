"""
loaders.py

프로젝트 요구사항 A

- CSV Loader
- PDF Loader
- Web Loader

모든 문서에 metadata 추가
"""

from pathlib import Path

from langchain_community.document_loaders import (
    CSVLoader,
    PyPDFLoader,
    WebBaseLoader
)

from langchain_core.documents import Document


def load_csv_documents(csv_dir: str):

    docs = []

    csv_path = Path(csv_dir)

    for file in csv_path.glob("*.csv"):

        loader = CSVLoader(
            file_path=str(file),
            encoding="utf-8"
        )

        loaded_docs = loader.load()

        for doc in loaded_docs:

            doc.metadata.update({

                "source": file.name,
                "type": "csv",
                "author": "project_team"
            })

        docs.extend(loaded_docs)

    return docs


def load_pdf_documents(pdf_dir: str):

    docs = []

    pdf_path = Path(pdf_dir)

    for file in pdf_path.glob("*.pdf"):

        loader = PyPDFLoader(
            str(file)
        )

        loaded_docs = loader.load()

        for doc in loaded_docs:

            doc.metadata.update({

                "source": file.name,
                "type": "pdf",
                "author": "unknown"
            })

        docs.extend(loaded_docs)

    return docs


def load_web_documents(urls: list[str]):

    docs = []

    for url in urls:

        try:

            loader = WebBaseLoader(url)

            loaded_docs = loader.load()

            for doc in loaded_docs:

                doc.metadata.update({

                    "source": url,
                    "type": "web",
                    "author": "web"
                })

            docs.extend(loaded_docs)

        except Exception as e:

            print(
                f"[WEB ERROR] {url}"
            )

            print(e)

    return docs


def load_documents(data_dir="data/raw"):

    all_docs = []

    all_docs.extend(

        load_csv_documents(
            data_dir
        )
    )

    all_docs.extend(

        load_pdf_documents(
            f"{data_dir}/pdfs"
        )
    )

    try:

        with open(
            f"{data_dir}/urls.txt",
            encoding="utf-8"
        ) as f:

            urls = [

                line.strip()

                for line in f

                if line.strip()
            ]

        all_docs.extend(

            load_web_documents(
                urls
            )
        )

    except FileNotFoundError:

        print(
            "urls.txt not found"
        )

    print(
        f"Loaded Documents: {len(all_docs)}"
    )

    return all_docs


if __name__ == "__main__":

    docs = load_documents()

    print(docs[0].metadata)