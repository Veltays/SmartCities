const path = require("path");
const vscode = require("vscode");
const { findNearestMicroPicoProject } = require("./nearest-project");

let uploadInProgress = false;

async function uploadNearestMicroPicoProject() {
    if (uploadInProgress) {
        return;
    }

    const editor = vscode.window.activeTextEditor;
    if (!editor || editor.document.uri.scheme !== "file") {
        void vscode.window.showWarningMessage(
            "Ouvrez un fichier du projet MicroPico à envoyer.",
        );
        return;
    }

    const workspaceFolder = vscode.workspace.getWorkspaceFolder(
        editor.document.uri,
    );
    if (!workspaceFolder) {
        void vscode.window.showWarningMessage(
            "Le fichier actif ne se trouve pas dans l’espace de travail.",
        );
        return;
    }

    const projectFolder = findNearestMicroPicoProject(
        editor.document.uri.fsPath,
        workspaceFolder.uri.fsPath,
    );
    if (!projectFolder) {
        void vscode.window.showWarningMessage(
            "Aucun fichier .micropico trouvé dans les dossiers parents.",
        );
        return;
    }

    uploadInProgress = true;
    const config = vscode.workspace.getConfiguration("micropico");
    const previousWorkspaceValue = config.inspect("syncFolder")?.workspaceValue;
    const relativeProjectFolder = path
        .relative(workspaceFolder.uri.fsPath, projectFolder)
        .replaceAll(path.sep, "/");

    try {
        if (editor.document.isDirty) {
            await editor.document.save();
        }

        await config.update(
            "syncFolder",
            relativeProjectFolder || ".",
            vscode.ConfigurationTarget.Workspace,
        );
        await vscode.commands.executeCommand("micropico.upload");
    } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        void vscode.window.showErrorMessage(`Échec de l’envoi MicroPico : ${message}`);
    } finally {
        try {
            await config.update(
                "syncFolder",
                previousWorkspaceValue,
                vscode.ConfigurationTarget.Workspace,
            );
        } finally {
            uploadInProgress = false;
        }
    }
}

function activate(context) {
    context.subscriptions.push(
        vscode.commands.registerCommand(
            "smartcities.uploadNearestMicroPico",
            uploadNearestMicroPicoProject,
        ),
    );
}

function deactivate() {}

module.exports = { activate, deactivate };
