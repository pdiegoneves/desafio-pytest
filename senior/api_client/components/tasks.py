import pandas as pd
import requests
import streamlit as st


def tasks():
    # Carregar tarefas da API
    response = requests.get("http://127.0.0.1:8000/api/tasks")
    tasks_data = response.json()

    # Converter para DataFrame
    df = pd.DataFrame(tasks_data)
    df = df.sort_values(["completed", "id"], ignore_index=True)

    # Se o DataFrame não estiver vazio
    if not df.empty:
        # Garantir que as colunas estão na ordem correta e com os tipos corretos
        df = df[["id", "title", "completed"]]

        # Converter tipos numpy para tipos Python nativos (importante para serialização)
        df["completed"] = df["completed"].astype(bool)

        # Configurar o editor de dados
        edited_df = st.data_editor(
            df,
            column_config={
                "id": st.column_config.NumberColumn("ID", disabled=True),
                "title": st.column_config.TextColumn("Título"),
                "completed": st.column_config.CheckboxColumn("Concluída"),
            },
            hide_index=True,
            key="task_editor",
        )

        # Verificar se houve mudanças no DataFrame
        if st.session_state.task_editor:
            # Obter as alterações
            changes = st.session_state.task_editor["edited_rows"]

            # Para cada linha alterada
            for idx, changed_values in changes.items():
                task_id = int(df.iloc[int(idx)]["id"])  # Garantir que seja int puro
                current_title = str(
                    df.iloc[int(idx)]["title"]
                )  # Garantir que seja string pura
                current_completed = bool(
                    df.iloc[int(idx)]["completed"]
                )  # Garantir que seja bool puro

                # Preparar os dados para a atualização
                update_data = {}

                # Se a coluna 'title' foi alterada
                if "title" in changed_values:
                    update_data["title"] = str(changed_values["title"])
                else:
                    update_data["title"] = current_title

                # Se a coluna 'completed' foi alterada
                if "completed" in changed_values:
                    update_data["completed"] = bool(changed_values["completed"])
                else:
                    update_data["completed"] = current_completed

                # Enviar PATCH request para a API apenas se houve alterações
                if "title" in changed_values or "completed" in changed_values:
                    # Converter para tipos Python nativos antes de serializar
                    update_data_json = {
                        "title": update_data["title"],
                        "completed": update_data["completed"],
                    }

                    response = requests.patch(
                        f"http://127.0.0.1:8000/api/tasks/{task_id}",
                        json=update_data_json,
                    )

                    if response.status_code == 200:
                        st.success(f"Tarefa {task_id} atualizada com sucesso!")
                        st.rerun()

                    else:
                        st.error(
                            f"Erro ao atualizar tarefa {task_id}: {response.status_code} - {response.text}"
                        )
    else:
        st.info("Nenhuma tarefa encontrada.")


def add_task():
    st.header("Adicionar tarefa")
    title = st.text_input("Tarefa", key="tarefa")

    if st.button("Adicionar"):
        if title:
            response = requests.post(
                "http://127.0.0.1:8000/api/tasks",
                json={"title": title, "completed": False},
            )
            if response.status_code == 200:
                st.success("Tarefa adicionada com sucesso")
                st.rerun()
            else:
                st.error(
                    f"Erro ao adicionar tarefa: {response.status_code} - {response.text}"
                )
        else:
            st.warning("Digite um título para a tarefa")
