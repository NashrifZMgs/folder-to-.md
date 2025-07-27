# Combined Code for `veditor-modern`

### Project Structure

<pre>.
├── 📦 <a href="#packagejson"><code>package.json</code></a>
└── 📁 packages/
    ├── 📁 backend/
    │   ├── 📦 <a href="#packagesbackendpackagejson"><code>package.json</code></a>
    │   ├── 📦 <a href="#packagesbackendtsconfigjson"><code>tsconfig.json</code></a>
    │   └── 📁 src/
    │       ├── 💻 <a href="#packagesbackendsrcindexts"><code>index.ts</code></a>
    │       ├── 💻 <a href="#packagesbackendsrctestfilets"><code>test-file.ts</code></a>
    │       └── 📁 services/
    │           └── 💻 <a href="#packagesbackendsrcservicesffmpegservicets"><code>ffmpeg.service.ts</code></a>
    └── 📁 frontend/
        ├── 🚫 <a href="#packagesfrontendgitignore"><code>.gitignore</code></a>
        ├── 📝 <a href="#packagesfrontendreadmemd"><code>README.md</code></a>
        ├── 📦 <a href="#packagesfrontendcomponentsjson"><code>components.json</code></a>
        ├── 💻 <a href="#packagesfrontendeslintconfigjs"><code>eslint.config.js</code></a>
        ├── 🌐 <a href="#packagesfrontendindexhtml"><code>index.html</code></a>
        ├── 📦 <a href="#packagesfrontendpackagejson"><code>package.json</code></a>
        ├── 📄 <a href="#packagesfrontendpostcssconfigcjs"><code>postcss.config.cjs</code></a>
        ├── 📄 <a href="#packagesfrontendtailwindconfigcjs"><code>tailwind.config.cjs</code></a>
        ├── 💻 <a href="#packagesfrontendtailwindconfigjs"><code>tailwind.config.js</code></a>
        ├── 📦 <a href="#packagesfrontendtsconfigappjson"><code>tsconfig.app.json</code></a>
        ├── 📦 <a href="#packagesfrontendtsconfigjson"><code>tsconfig.json</code></a>
        ├── 📦 <a href="#packagesfrontendtsconfignodejson"><code>tsconfig.node.json</code></a>
        ├── 💻 <a href="#packagesfrontendviteconfigts"><code>vite.config.ts</code></a>
        ├── 📁 public/
        │   └── 📄 <a href="#packagesfrontendpublicvitesvg"><code>vite.svg</code></a>
        └── 📁 src/
            ├── 🎨 <a href="#packagesfrontendsrcappcss"><code>App.css</code></a>
            ├── 💻 <a href="#packagesfrontendsrcapptsx"><code>App.tsx</code></a>
            ├── 🎨 <a href="#packagesfrontendsrcindexcss"><code>index.css</code></a>
            ├── 💻 <a href="#packagesfrontendsrcmaintsx"><code>main.tsx</code></a>
            ├── 💻 <a href="#packagesfrontendsrcviteenvdts"><code>vite-env.d.ts</code></a>
            ├── 📁 assets/
            │   └── 📄 <a href="#packagesfrontendsrcassetsreactsvg"><code>react.svg</code></a>
            ├── 📁 components/
            │   ├── 📁 editor/
            │   │   ├── 💻 <a href="#packagesfrontendsrccomponentseditoraddvideomodaltsx"><code>AddVideoModal.tsx</code></a>
            │   │   ├── 💻 <a href="#packagesfrontendsrccomponentseditoreditorlayouttsx"><code>EditorLayout.tsx</code></a>
            │   │   ├── 💻 <a href="#packagesfrontendsrccomponentseditorglobalsettingspaneltsx"><code>GlobalSettingsPanel.tsx</code></a>
            │   │   ├── 💻 <a href="#packagesfrontendsrccomponentseditormediapaneltsx"><code>MediaPanel.tsx</code></a>
            │   │   ├── 💻 <a href="#packagesfrontendsrccomponentseditoroutputlibrarytsx"><code>OutputLibrary.tsx</code></a>
            │   │   ├── 💻 <a href="#packagesfrontendsrccomponentseditorplayerpaneltsx"><code>PlayerPanel.tsx</code></a>
            │   │   ├── 💻 <a href="#packagesfrontendsrccomponentseditorprocessingstatustsx"><code>ProcessingStatus.tsx</code></a>
            │   │   ├── 💻 <a href="#packagesfrontendsrccomponentseditorqueuepaneltsx"><code>QueuePanel.tsx</code></a>
            │   │   └── 💻 <a href="#packagesfrontendsrccomponentseditorsettingspaneltsx"><code>SettingsPanel.tsx</code></a>
            │   └── 📁 ui/
            │       ├── 💻 <a href="#packagesfrontendsrccomponentsuiaccordiontsx"><code>accordion.tsx</code></a>
            │       ├── 💻 <a href="#packagesfrontendsrccomponentsuibuttontsx"><code>button.tsx</code></a>
            │       ├── 💻 <a href="#packagesfrontendsrccomponentsuicardtsx"><code>card.tsx</code></a>
            │       ├── 💻 <a href="#packagesfrontendsrccomponentsuidialogtsx"><code>dialog.tsx</code></a>
            │       ├── 💻 <a href="#packagesfrontendsrccomponentsuiinputtsx"><code>input.tsx</code></a>
            │       ├── 💻 <a href="#packagesfrontendsrccomponentsuilabeltsx"><code>label.tsx</code></a>
            │       ├── 💻 <a href="#packagesfrontendsrccomponentsuiprogresstsx"><code>progress.tsx</code></a>
            │       ├── 💻 <a href="#packagesfrontendsrccomponentsuiresizabletsx"><code>resizable.tsx</code></a>
            │       ├── 💻 <a href="#packagesfrontendsrccomponentsuiselecttsx"><code>select.tsx</code></a>
            │       ├── 💻 <a href="#packagesfrontendsrccomponentsuislidertsx"><code>slider.tsx</code></a>
            │       ├── 💻 <a href="#packagesfrontendsrccomponentsuiswitchtsx"><code>switch.tsx</code></a>
            │       ├── 💻 <a href="#packagesfrontendsrccomponentsuitabstsx"><code>tabs.tsx</code></a>
            │       └── 💻 <a href="#packagesfrontendsrccomponentsuivariantsts"><code>variants.ts</code></a>
            ├── 📁 lib/
            │   ├── 💻 <a href="#packagesfrontendsrclibsocketts"><code>socket.ts</code></a>
            │   └── 💻 <a href="#packagesfrontendsrclibutilsts"><code>utils.ts</code></a>
            ├── 📁 pages/
            │   ├── 💻 <a href="#packagesfrontendsrcpagesdashboardpagetsx"><code>DashboardPage.tsx</code></a>
            │   └── 💻 <a href="#packagesfrontendsrcpageseditorpagetsx"><code>EditorPage.tsx</code></a>
            └── 📁 stores/
                ├── 💻 <a href="#packagesfrontendsrcstoresuseprocessingstorets"><code>useProcessingStore.ts</code></a>
                ├── 💻 <a href="#packagesfrontendsrcstoresuseprojectstorets"><code>useProjectStore.ts</code></a>
                ├── 💻 <a href="#packagesfrontendsrcstoresusequeuestorets"><code>useQueueStore.ts</code></a>
                ├── 💻 <a href="#packagesfrontendsrcstoresusesettingsstorets"><code>useSettingsStore.ts</code></a>
                └── 💻 <a href="#packagesfrontendsrcstoresusevideoplayerstorets"><code>useVideoPlayerStore.ts</code></a></pre>

---
---

<h2 id="packagejson"><code>package.json</code></h2>

```json
{
  "name": "veditor-modern-root",
  "version": "1.0.0",
  "private": true,
  "description": "Root for the modern Veditor project",
  "main": "index.js",
  "scripts": {
    "dev": "concurrently \"npm:dev --workspace=packages/backend\" \"npm:dev --workspace=packages/frontend\"",
    "install:all": "npm install && npm install --workspace=packages/frontend && npm install --workspace=packages/backend"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "workspaces": [
    "packages/*"
  ],
  "devDependencies": {
    "concurrently": "^8.2.2"
  }
}
```

---

<h2 id="packagesbackendpackagejson"><code>packages/backend/package.json</code></h2>

```json
{
  "name": "backend",
  "version": "1.0.0",
  "description": "The Node.js backend for Veditor",
  "main": "dist/index.js",
  "scripts": {
    "build": "tsc",
    "dev": "ts-node-dev --respawn --transpile-only src/index.ts"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "cors": "^2.8.5",
    "express": "^4.18.2",
    "multer": "^2.0.2",
    "socket.io": "^4.8.1",
    "yt-dlp-wrap": "^2.3.12"
  },
  "devDependencies": {
    "@types/cors": "^2.8.17",
    "@types/express": "^4.17.21",
    "@types/multer": "^2.0.0",
    "@types/node": "^20.11.24",
    "ts-node-dev": "^2.0.0",
    "typescript": "^5.3.3"
  }
}

```

---

<h2 id="packagesbackendsrcindexts"><code>packages/backend/src/index.ts</code></h2>

```typescript
import express, { Request, Response } from 'express';
import http from 'http';
import { Server as SocketIOServer } from 'socket.io';
import cors from 'cors';
import fs from 'fs/promises';
import fsSync from 'fs';
import path from 'path';
import multer from 'multer';
import YTDlpWrap from 'yt-dlp-wrap';
import { FfmpegService } from './services/ffmpeg.service';

const app = express();
const server = http.createServer(app);
const io = new SocketIOServer(server, {
  cors: {
    origin: "http://localhost:5173", // Your frontend URL
    methods: ["GET", "POST"]
  }
});

const port = 5001;

// --- PATHS & CONFIG ---
const rootDir = path.join(__dirname, '..', '..', '..'); 
const projectsRoot = path.join(rootDir, 'projects');
const ytdlpPath = path.join(rootDir, 'yt-dlp'); 

// ... (yt-dlp setup code remains the same)
const ytdlp = new YTDlpWrap();
if (!fsSync.existsSync(ytdlpPath)) {
    fsSync.mkdirSync(ytdlpPath);
}
YTDlpWrap.downloadFromGithub(path.join(ytdlpPath, 'yt-dlp')).then(() => {
    ytdlp.setBinaryPath(path.join(ytdlpPath, 'yt-dlp'));
    console.log('yt-dlp binary downloaded and set up.');
});

app.use(cors());
app.use(express.json());

// --- MULTER SETUP (remains the same) ---
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    const projectPath = path.join(projectsRoot, req.params.projectName);
    cb(null, projectPath);
  },
  filename: (req, file, cb) => { cb(null, file.originalname); }
});
const upload = multer({ storage: storage });

// --- STATIC FILE SERVING (remains the same) ---
app.use('/videos', express.static(projectsRoot));

// =================================================================
// --- API ENDPOINTS ---
// =================================================================

// Health check
app.get('/api/health', (req: Request, res: Response) => {
  res.status(200).json({ status: 'Backend is running!' });
});

// GET /api/projects
app.get('/api/projects', async (req: Request, res: Response) => {
  try {
    await fs.mkdir(projectsRoot, { recursive: true });
    const allFiles = await fs.readdir(projectsRoot, { withFileTypes: true });
    const directories = allFiles.filter(dirent => dirent.isDirectory()).map(dirent => dirent.name);
    res.status(200).json(directories);
  } catch (error) {
    console.error('Error fetching projects:', error);
    res.status(500).json({ message: 'Failed to fetch projects.' });
  }
});

// POST /api/projects
app.post('/api/projects', async (req: Request, res: Response) => {
    const { projectName } = req.body;
    if (!projectName || !/^[a-z0-9-]+$/.test(projectName)) {
        return res.status(400).json({ message: 'Invalid project name.' });
    }
    try {
        const projectPath = path.join(projectsRoot, projectName);
        await fs.mkdir(projectPath, { recursive: true });
        res.status(201).json({ message: 'Project created successfully.', projectName });
    } catch (error) {
        console.error('Error creating project:', error);
        res.status(500).json({ message: 'Failed to create project.' });
    }
});

// POST /api/projects/:projectName/save-state
app.post('/api/projects/:projectName/save-state', async (req: Request, res: Response) => {
    const { projectName } = req.params;
    const { queue, settings } = req.body;
    
    if (!queue || !settings) {
        return res.status(400).json({ message: 'Queue and settings are required.' });
    }
    
    const projectPath = path.join(projectsRoot, projectName);
    const stateFilePath = path.join(projectPath, 'autosave.json');

    try {
        await fs.writeFile(stateFilePath, JSON.stringify({ queue, settings }, null, 2));
        res.status(200).json({ message: 'State saved successfully.' });
    } catch (error) {
        console.error('Error saving project state:', error);
        res.status(500).json({ message: 'Failed to save project state.' });
    }
});

// GET /api/projects/:projectName/videos
app.get('/api/projects/:projectName/videos', async (req: Request, res: Response) => {
    const { projectName } = req.params;
    const projectPath = path.join(projectsRoot, projectName);
    try {
        const allFiles = await fs.readdir(projectPath);
        const videoFiles = allFiles.filter(f => /\.(mp4|mkv|mov|webm|avi)$/i.test(f));
        res.status(200).json(videoFiles);
    } catch (error) {
        console.error(`Error fetching videos for ${projectName}:`, error);
        res.status(500).json({ message: 'Failed to fetch videos.' });
    }
});

// POST /api/projects/:projectName/add-from-url
app.post('/api/projects/:projectName/add-from-url', async (req: Request, res: Response) => {
    const { projectName } = req.params;
    const { url } = req.body;
    if (!url) {
        return res.status(400).json({ message: 'URL is required.' });
    }

    const projectPath = path.join(projectsRoot, projectName);
    console.log(`Downloading video from ${url} into ${projectPath}`);
    
    try {
        await ytdlp.execPromise([
            url,
            '-o', `${projectPath}/%(title)s.%(ext)s`,
            '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        ]);
        res.status(200).json({ message: 'Video downloaded successfully!' });
    } catch (error) {
        console.error('yt-dlp error:', error);
        res.status(500).json({ message: 'Failed to download video.' });
    }
});

// POST /api/projects/:projectName/upload
app.post('/api/projects/:projectName/upload', upload.single('video'), (req: Request, res: Response) => {
    if (!req.file) {
        return res.status(400).json({ message: 'No file uploaded.' });
    }
    res.status(200).json({ message: 'File uploaded successfully!', filename: req.file.filename });
});

/**
 * GET /api/projects/:projectName/outputs
 * Returns a list of processed video files.
 */
app.get('/api/projects/:projectName/outputs', async (req: Request, res: Response) => {
    const { projectName } = req.params;
    const outputDir = path.join(projectsRoot, projectName, 'output');
    try {
        await fs.mkdir(outputDir, { recursive: true });
        const allFiles = await fs.readdir(outputDir);
        const videoFiles = allFiles.filter(f => /\.(mp4|mkv|mov|webm|avi|gif)$/i.test(f));
        res.status(200).json(videoFiles);
    } catch (error) {
        res.status(500).json({ message: 'Failed to fetch output videos.' });
    }
});
// =================================================================


// --- SOCKET.IO LOGIC ---
io.on('connection', (socket) => {
  console.log('A user connected:', socket.id);

  socket.on('start-processing', async ({ queue, settings, projectName }) => {
    console.log(`[${socket.id}] Received start-processing for project: ${projectName}`);
    const projectPath = path.join(projectsRoot, projectName);
    
    const ffmpegService = new FfmpegService();

    ffmpegService.on('progress', (progress) => {
      socket.emit('processing-progress', { progress });
    });

    ffmpegService.on('log', (log) => {
      socket.emit('processing-log', { log });
    });

    ffmpegService.on('done', (result) => {
      if (result.success) {
        socket.emit('processing-complete', { path: result.outputPath });
      } else {
        socket.emit('processing-error', { message: result.message });
      }
    });

    try {
        await ffmpegService.processQueue(queue, settings, projectPath, projectsRoot);
    } catch (error: any) {
        socket.emit('processing-error', { message: error.message });
    }
  });

  socket.on('disconnect', () => {
    console.log('User disconnected:', socket.id);
  });
});


// --- SERVER START ---
// Use the http server to listen, not the express app
server.listen(port, () => {
  console.log(`Backend server with Socket.IO listening at http://localhost:${port}`);
});

```

---

<h2 id="packagesbackendsrcservicesffmpegservicets"><code>packages/backend/src/services/ffmpeg.service.ts</code></h2>

```typescript
import { spawn } from 'child_process';
import EventEmitter from 'events';
import path from 'path';
import fs from 'fs/promises';

// These types should match the ones in your frontend stores
interface Clip {
  id: string;
  sourceVideo: string;
  startTime: number;
  endTime: number;
}

interface FFmpegSettings {
  outputFormat: 'mp4' | 'mov' | 'gif';
  videoCodec: 'H.264 (libx264)' | 'H.265 (libx265)';
  audioCodec: 'AAC' | 'MP3';
  quality: number;
  encodingSpeed: 'ultrafast' | 'fast' | 'medium' | 'slow';
  combineClips: boolean;
}

export class FfmpegService extends EventEmitter {
  private getCodec(settings: FFmpegSettings) {
    const videoCodecs = {
      'H.264 (libx264)': 'libx264',
      'H.265 (libx265)': 'libx265',
    };
    const audioCodecs = {
      'AAC': 'aac',
      'MP3': 'libmp3lame',
    };
    return {
      vcodec: videoCodecs[settings.videoCodec],
      acodec: audioCodecs[settings.audioCodec],
    };
  }

  private parseProgress(data: string, totalDuration: number) {
    const timeMatch = data.match(/time=(\d{2}):(\d{2}):(\d{2})\.(\d{2})/);
    if (timeMatch) {
      const hours = parseInt(timeMatch[1], 10);
      const minutes = parseInt(timeMatch[2], 10);
      const seconds = parseInt(timeMatch[3], 10);
      const ms = parseInt(timeMatch[4], 10) * 10;
      const currentTime = hours * 3600 + minutes * 60 + seconds + ms / 1000;
      const progress = Math.min(100, Math.floor((currentTime / totalDuration) * 100));
      return progress;
    }
    return null;
  }
  
  public async processQueue(queue: Clip[], settings: FFmpegSettings, projectPath: string, projectsRoot: string) {
    const outputDir = path.join(projectPath, 'output');
    await fs.mkdir(outputDir, { recursive: true });

    const { vcodec, acodec } = this.getCodec(settings);
    const totalDuration = queue.reduce((acc, clip) => acc + (clip.endTime - clip.startTime), 0);
    const outputFilename = `output_${new Date().getTime()}.${settings.outputFormat}`;
    const outputPath = path.join(outputDir, outputFilename);

    const args: string[] = ['-y']; // Overwrite output file if it exists

    // Input files
    queue.forEach(clip => {
        // Source video path is like `/videos/project-name/video.mp4`
        // We need to map it to the actual file system path
        const relativePath = clip.sourceVideo.replace('/videos/', '');
        const fullPath = path.join(projectsRoot, relativePath);
        args.push('-i', fullPath);
    });

    if (settings.combineClips && queue.length > 1) {
        // CONCATENATE CLIPS
        let filterComplex = '';
        let filterOutputs = '';
        queue.forEach((clip, index) => {
            filterComplex += `[${index}:v]trim=start=${clip.startTime}:end=${clip.endTime},setpts=PTS-STARTPTS[v${index}];`;
            filterComplex += `[${index}:a]atrim=start=${clip.startTime}:end=${clip.endTime},asetpts=PTS-STARTPTS[a${index}];`;
            filterOutputs += `[v${index}][a${index}]`;
        });
        filterComplex += `${filterOutputs}concat=n=${queue.length}:v=1:a=1[outv][outa]`;
        
        args.push(
            '-filter_complex', filterComplex,
            '-map', '[outv]',
            '-map', '[outa]'
        );
    } else {
        // SINGLE CLIP (OR NON-COMBINED)
        const clip = queue[0];
        args.push(
            '-ss', clip.startTime.toString(),
            '-to', clip.endTime.toString()
        );
    }

    // Add output settings
    args.push(
        '-c:v', vcodec,
        '-crf', settings.quality.toString(),
        '-preset', settings.encodingSpeed,
        '-c:a', acodec,
        outputPath
    );

    this.emit('log', `Executing ffmpeg with args: ${args.join(' ')}`);

    const ffmpeg = spawn('ffmpeg', args);

    ffmpeg.stderr.on('data', (data: Buffer) => {
      const line = data.toString();
      this.emit('log', line);
      const progress = this.parseProgress(line, totalDuration);
      if (progress !== null) {
        this.emit('progress', progress);
      }
    });

    ffmpeg.on('close', (code) => {
      if (code === 0) {
        this.emit('done', { success: true, outputPath: `/videos/${path.basename(projectPath)}/output/${outputFilename}` });
      } else {
        this.emit('done', { success: false, message: `ffmpeg exited with code ${code}` });
      }
    });

    ffmpeg.on('error', (err) => {
      this.emit('log', `ffmpeg error: ${err.message}`);
      this.emit('done', { success: false, message: `ffmpeg failed to start: ${err.message}` });
    });
  }
}

```

---

<h2 id="packagesbackendsrctestfilets"><code>packages/backend/src/test-file.ts</code></h2>

```typescript
// This is a test file.

```

---

<h2 id="packagesbackendtsconfigjson"><code>packages/backend/tsconfig.json</code></h2>

```json
{
  "compilerOptions": {
    "target": "ES6",
    "module": "commonjs",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true
  },
  "include": ["src/**/*"]
}
```

---

<h2 id="packagesfrontendgitignore"><code>packages/frontend/.gitignore</code></h2>

```
# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

node_modules
dist
dist-ssr
*.local

# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?

```

---

<h2 id="packagesfrontendreadmemd"><code>packages/frontend/README.md</code></h2>

```markdown
# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type-aware lint rules:

```js
export default tseslint.config([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...

      // Remove tseslint.configs.recommended and replace with this
      ...tseslint.configs.recommendedTypeChecked,
      // Alternatively, use this for stricter rules
      ...tseslint.configs.strictTypeChecked,
      // Optionally, add this for stylistic rules
      ...tseslint.configs.stylisticTypeChecked,

      // Other configs...
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```

You can also install [eslint-plugin-react-x](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-x) and [eslint-plugin-react-dom](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-dom) for React-specific lint rules:

```js
// eslint.config.js
import reactX from 'eslint-plugin-react-x'
import reactDom from 'eslint-plugin-react-dom'

export default tseslint.config([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...
      // Enable lint rules for React
      reactX.configs['recommended-typescript'],
      // Enable lint rules for React DOM
      reactDom.configs.recommended,
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```

```

---

<h2 id="packagesfrontendcomponentsjson"><code>packages/frontend/components.json</code></h2>

```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": false,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "src/index.css",
    "baseColor": "neutral",
    "cssVariables": true,
    "prefix": ""
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  },
  "iconLibrary": "lucide"
}
```

---

<h2 id="packagesfrontendeslintconfigjs"><code>packages/frontend/eslint.config.js</code></h2>

```javascript
import js from '@eslint/js'
import globals from 'globals'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'
import tseslint from 'typescript-eslint'
import { globalIgnores } from 'eslint/config'

export default tseslint.config([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      js.configs.recommended,
      tseslint.configs.recommended,
      reactHooks.configs['recommended-latest'],
      reactRefresh.configs.vite,
    ],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
    },
  },
])

```

---

<h2 id="packagesfrontendindexhtml"><code>packages/frontend/index.html</code></h2>

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite + React + TS</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>

```

---

<h2 id="packagesfrontendpackagejson"><code>packages/frontend/package.json</code></h2>

```json
{
  "name": "frontend",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  },
  "dependencies": {
    "@dnd-kit/core": "^6.3.1",
    "@dnd-kit/sortable": "^10.0.0",
    "@radix-ui/react-accordion": "^1.2.11",
    "@radix-ui/react-dialog": "^1.1.14",
    "@radix-ui/react-label": "^2.1.7",
    "@radix-ui/react-progress": "^1.1.7",
    "@radix-ui/react-select": "^2.2.5",
    "@radix-ui/react-slider": "^1.3.5",
    "@radix-ui/react-slot": "^1.2.3",
    "@radix-ui/react-switch": "^1.2.5",
    "@radix-ui/react-tabs": "^1.1.12",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "lucide-react": "^0.525.0",
    "react": "^19.1.0",
    "react-dom": "^19.1.0",
    "react-player": "^3.3.1",
    "react-resizable-panels": "^3.0.3",
    "react-router-dom": "^7.7.1",
    "socket.io-client": "^4.8.1",
    "tailwind-merge": "^3.3.1",
    "uuid": "^11.1.0",
    "zustand": "^5.0.6"
  },
  "devDependencies": {
    "@eslint/js": "^9.30.1",
    "@tailwindcss/postcss": "^4.1.11",
    "@types/react": "^19.1.8",
    "@types/react-dom": "^19.1.6",
    "@types/uuid": "^10.0.0",
    "@vitejs/plugin-react": "^4.6.0",
    "autoprefixer": "^10.4.21",
    "eslint": "^9.30.1",
    "eslint-plugin-react-hooks": "^5.2.0",
    "eslint-plugin-react-refresh": "^0.4.20",
    "globals": "^16.3.0",
    "postcss": "^8.5.6",
    "tailwindcss": "^4.1.11",
    "tw-animate-css": "^1.3.6",
    "typescript": "~5.8.3",
    "typescript-eslint": "^8.35.1",
    "vite": "^7.0.4"
  }
}

```

---

<h2 id="packagesfrontendpostcssconfigcjs"><code>packages/frontend/postcss.config.cjs</code></h2>

```
module.exports = {
  plugins: {
    '@tailwindcss/postcss': {},
    'autoprefixer': {},
  },
};
```

---

<h2 id="packagesfrontendpublicvitesvg"><code>packages/frontend/public/vite.svg</code></h2>

```
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="iconify iconify--logos" width="31.88" height="32" preserveAspectRatio="xMidYMid meet" viewBox="0 0 256 257"><defs><linearGradient id="IconifyId1813088fe1fbc01fb466" x1="-.828%" x2="57.636%" y1="7.652%" y2="78.411%"><stop offset="0%" stop-color="#41D1FF"></stop><stop offset="100%" stop-color="#BD34FE"></stop></linearGradient><linearGradient id="IconifyId1813088fe1fbc01fb467" x1="43.376%" x2="50.316%" y1="2.242%" y2="89.03%"><stop offset="0%" stop-color="#FFEA83"></stop><stop offset="8.333%" stop-color="#FFDD35"></stop><stop offset="100%" stop-color="#FFA800"></stop></linearGradient></defs><path fill="url(#IconifyId1813088fe1fbc01fb466)" d="M255.153 37.938L134.897 252.976c-2.483 4.44-8.862 4.466-11.382.048L.875 37.958c-2.746-4.814 1.371-10.646 6.827-9.67l120.385 21.517a6.537 6.537 0 0 0 2.322-.004l117.867-21.483c5.438-.991 9.574 4.796 6.877 9.62Z"></path><path fill="url(#IconifyId1813088fe1fbc01fb467)" d="M185.432.063L96.44 17.501a3.268 3.268 0 0 0-2.634 3.014l-5.474 92.456a3.268 3.268 0 0 0 3.997 3.378l24.777-5.718c2.318-.535 4.413 1.507 3.936 3.838l-7.361 36.047c-.495 2.426 1.782 4.5 4.151 3.78l15.304-4.649c2.372-.72 4.652 1.36 4.15 3.788l-11.698 56.621c-.732 3.542 3.979 5.473 5.943 2.437l1.313-2.028l72.516-144.72c1.215-2.423-.88-5.186-3.54-4.672l-25.505 4.922c-2.396.462-4.435-1.77-3.759-4.114l16.646-57.705c.677-2.35-1.37-4.583-3.769-4.113Z"></path></svg>
```

---

<h2 id="packagesfrontendsrcappcss"><code>packages/frontend/src/App.css</code></h2>

```css
#root {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}

.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.react:hover {
  filter: drop-shadow(0 0 2em #61dafbaa);
}

@keyframes logo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: no-preference) {
  a:nth-of-type(2) .logo {
    animation: logo-spin infinite 20s linear;
  }
}

.card {
  padding: 2em;
}

.read-the-docs {
  color: #888;
}

```

---

<h2 id="packagesfrontendsrcapptsx"><code>packages/frontend/src/App.tsx</code></h2>

```typescript
import { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import DashboardPage from './pages/DashboardPage';
import EditorPage from './pages/EditorPage';

function App() {
  // This effect ensures the dark theme is applied to the root HTML element
  useEffect(() => {
    const root = window.document.documentElement;
    root.classList.add('dark');
  }, []);

  return (
    <Router>
      <div className="bg-background text-foreground min-h-screen">
        <Routes>
          <Route path="/" element={<DashboardPage />} />
          <Route path="/editor/:projectName" element={<EditorPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

```

---

<h2 id="packagesfrontendsrcassetsreactsvg"><code>packages/frontend/src/assets/react.svg</code></h2>

```
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="iconify iconify--logos" width="35.93" height="32" preserveAspectRatio="xMidYMid meet" viewBox="0 0 256 228"><path fill="#00D8FF" d="M210.483 73.824a171.49 171.49 0 0 0-8.24-2.597c.465-1.9.893-3.777 1.273-5.621c6.238-30.281 2.16-54.676-11.769-62.708c-13.355-7.7-35.196.329-57.254 19.526a171.23 171.23 0 0 0-6.375 5.848a155.866 155.866 0 0 0-4.241-3.917C100.759 3.829 77.587-4.822 63.673 3.233C50.33 10.957 46.379 33.89 51.995 62.588a170.974 170.974 0 0 0 1.892 8.48c-3.28.932-6.445 1.924-9.474 2.98C17.309 83.498 0 98.307 0 113.668c0 15.865 18.582 31.778 46.812 41.427a145.52 145.52 0 0 0 6.921 2.165a167.467 167.467 0 0 0-2.01 9.138c-5.354 28.2-1.173 50.591 12.134 58.266c13.744 7.926 36.812-.22 59.273-19.855a145.567 145.567 0 0 0 5.342-4.923a168.064 168.064 0 0 0 6.92 6.314c21.758 18.722 43.246 26.282 56.54 18.586c13.731-7.949 18.194-32.003 12.4-61.268a145.016 145.016 0 0 0-1.535-6.842c1.62-.48 3.21-.974 4.76-1.488c29.348-9.723 48.443-25.443 48.443-41.52c0-15.417-17.868-30.326-45.517-39.844Zm-6.365 70.984c-1.4.463-2.836.91-4.3 1.345c-3.24-10.257-7.612-21.163-12.963-32.432c5.106-11 9.31-21.767 12.459-31.957c2.619.758 5.16 1.557 7.61 2.4c23.69 8.156 38.14 20.213 38.14 29.504c0 9.896-15.606 22.743-40.946 31.14Zm-10.514 20.834c2.562 12.94 2.927 24.64 1.23 33.787c-1.524 8.219-4.59 13.698-8.382 15.893c-8.067 4.67-25.32-1.4-43.927-17.412a156.726 156.726 0 0 1-6.437-5.87c7.214-7.889 14.423-17.06 21.459-27.246c12.376-1.098 24.068-2.894 34.671-5.345a134.17 134.17 0 0 1 1.386 6.193ZM87.276 214.515c-7.882 2.783-14.16 2.863-17.955.675c-8.075-4.657-11.432-22.636-6.853-46.752a156.923 156.923 0 0 1 1.869-8.499c10.486 2.32 22.093 3.988 34.498 4.994c7.084 9.967 14.501 19.128 21.976 27.15a134.668 134.668 0 0 1-4.877 4.492c-9.933 8.682-19.886 14.842-28.658 17.94ZM50.35 144.747c-12.483-4.267-22.792-9.812-29.858-15.863c-6.35-5.437-9.555-10.836-9.555-15.216c0-9.322 13.897-21.212 37.076-29.293c2.813-.98 5.757-1.905 8.812-2.773c3.204 10.42 7.406 21.315 12.477 32.332c-5.137 11.18-9.399 22.249-12.634 32.792a134.718 134.718 0 0 1-6.318-1.979Zm12.378-84.26c-4.811-24.587-1.616-43.134 6.425-47.789c8.564-4.958 27.502 2.111 47.463 19.835a144.318 144.318 0 0 1 3.841 3.545c-7.438 7.987-14.787 17.08-21.808 26.988c-12.04 1.116-23.565 2.908-34.161 5.309a160.342 160.342 0 0 1-1.76-7.887Zm110.427 27.268a347.8 347.8 0 0 0-7.785-12.803c8.168 1.033 15.994 2.404 23.343 4.08c-2.206 7.072-4.956 14.465-8.193 22.045a381.151 381.151 0 0 0-7.365-13.322Zm-45.032-43.861c5.044 5.465 10.096 11.566 15.065 18.186a322.04 322.04 0 0 0-30.257-.006c4.974-6.559 10.069-12.652 15.192-18.18ZM82.802 87.83a323.167 323.167 0 0 0-7.227 13.238c-3.184-7.553-5.909-14.98-8.134-22.152c7.304-1.634 15.093-2.97 23.209-3.984a321.524 321.524 0 0 0-7.848 12.897Zm8.081 65.352c-8.385-.936-16.291-2.203-23.593-3.793c2.26-7.3 5.045-14.885 8.298-22.6a321.187 321.187 0 0 0 7.257 13.246c2.594 4.48 5.28 8.868 8.038 13.147Zm37.542 31.03c-5.184-5.592-10.354-11.779-15.403-18.433c4.902.192 9.899.29 14.978.29c5.218 0 10.376-.117 15.453-.343c-4.985 6.774-10.018 12.97-15.028 18.486Zm52.198-57.817c3.422 7.8 6.306 15.345 8.596 22.52c-7.422 1.694-15.436 3.058-23.88 4.071a382.417 382.417 0 0 0 7.859-13.026a347.403 347.403 0 0 0 7.425-13.565Zm-16.898 8.101a358.557 358.557 0 0 1-12.281 19.815a329.4 329.4 0 0 1-23.444.823c-7.967 0-15.716-.248-23.178-.732a310.202 310.202 0 0 1-12.513-19.846h.001a307.41 307.41 0 0 1-10.923-20.627a310.278 310.278 0 0 1 10.89-20.637l-.001.001a307.318 307.318 0 0 1 12.413-19.761c7.613-.576 15.42-.876 23.31-.876H128c7.926 0 15.743.303 23.354.883a329.357 329.357 0 0 1 12.335 19.695a358.489 358.489 0 0 1 11.036 20.54a329.472 329.472 0 0 1-11 20.722Zm22.56-122.124c8.572 4.944 11.906 24.881 6.52 51.026c-.344 1.668-.73 3.367-1.15 5.09c-10.622-2.452-22.155-4.275-34.23-5.408c-7.034-10.017-14.323-19.124-21.64-27.008a160.789 160.789 0 0 1 5.888-5.4c18.9-16.447 36.564-22.941 44.612-18.3ZM128 90.808c12.625 0 22.86 10.235 22.86 22.86s-10.235 22.86-22.86 22.86s-22.86-10.235-22.86-22.86s10.235-22.86 22.86-22.86Z"></path></svg>
```

---

<h2 id="packagesfrontendsrccomponentseditoraddvideomodaltsx"><code>packages/frontend/src/components/editor/AddVideoModal.tsx</code></h2>

```typescript
import { useState } from 'react';
import { useProjectStore } from '@/stores/useProjectStore';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Progress } from "@/components/ui/progress";
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription } from "@/components/ui/dialog";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";

interface AddVideoModalProps {
  isOpen: boolean;
  onClose: () => void;
  onVideoAdded: () => void; // Callback to refresh the video list
}

export default function AddVideoModal({ isOpen, onClose, onVideoAdded }: AddVideoModalProps) {
  const projectName = useProjectStore((state) => state.projectName);
  const [url, setUrl] = useState('');
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleAddFromUrl = async () => {
    if (!url || !projectName) return;
    setIsLoading(true);
    setError('');
    try {
      const response = await fetch(`/api/projects/${projectName}/add-from-url`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url }),
      });
      if (!response.ok) throw new Error('Failed to download video from URL.');
      onVideoAdded(); // Refresh list on success
      onClose();
    } catch (err: unknown) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError('An unknown error occurred.');
      }
    } finally {
      setIsLoading(false);
    }
  };

  const handleUploadFile = async () => {
    if (!selectedFile || !projectName) return;
    setIsLoading(true);
    setError('');
    
    const formData = new FormData();
    formData.append('video', selectedFile);

    try {
      const response = await fetch(`/api/projects/${projectName}/upload`, {
        method: 'POST',
        body: formData,
      });
      if (!response.ok) throw new Error('Failed to upload file.');
      onVideoAdded();
      onClose();
    } catch (err: unknown) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError('An unknown error occurred.');
      }
    } finally {
      setIsLoading(false);
    }
  };
  
  const handleClose = () => {
      if (isLoading) return; // Prevent closing while loading
      setUrl('');
      setSelectedFile(null);
      setError('');
      onClose();
  }

  return (
    <Dialog open={isOpen} onOpenChange={handleClose}>
      <DialogContent className="bg-gray-800 border-gray-700 text-white">
        <DialogHeader>
          <DialogTitle>Add Videos to Start</DialogTitle>
          <DialogDescription>Add local files or paste a URL from the web.</DialogDescription>
        </DialogHeader>

        {isLoading ? (
            <div className="flex flex-col items-center justify-center p-8 space-y-4">
                <p>Processing your video...</p>
                <Progress value={undefined} className="w-[60%]" />
            </div>
        ) : (
            <Tabs defaultValue="url" className="w-full">
                <TabsList className="grid w-full grid-cols-2">
                    <TabsTrigger value="url">From URL</TabsTrigger>
                    <TabsTrigger value="upload">Upload File</TabsTrigger>
                </TabsList>

                {/* URL Tab */}
                <TabsContent value="url" className="space-y-4 pt-4">
                    <Label htmlFor="url">Video URL</Label>
                    <Input id="url" value={url} onChange={(e) => setUrl(e.target.value)} placeholder="https://..." className="bg-gray-900 border-gray-600"/>
                    <Button onClick={handleAddFromUrl} className="w-full">Add from URL</Button>
                </TabsContent>

                {/* Upload Tab */}
                <TabsContent value="upload" className="space-y-4 pt-4">
                    <Label htmlFor="picture">Local Video File</Label>
                    <Input id="picture" type="file" onChange={(e) => setSelectedFile(e.target.files?.[0] || null)} className="bg-gray-900 border-gray-600 file:text-white"/>
                    <Button onClick={handleUploadFile} className="w-full" disabled={!selectedFile}>Upload Video</Button>
                </TabsContent>
            </Tabs>
        )}
        {error && <p className="text-sm text-red-500 mt-2 text-center">{error}</p>}
      </DialogContent>
    </Dialog>
  );
}
```

---

<h2 id="packagesfrontendsrccomponentseditoreditorlayouttsx"><code>packages/frontend/src/components/editor/EditorLayout.tsx</code></h2>

```typescript
import {
  ResizablePanelGroup,
  ResizablePanel,
  ResizableHandle,
} from "@/components/ui/resizable";
import MediaPanel from "./MediaPanel";
import PlayerPanel from "./PlayerPanel";
import SettingsPanel from "./SettingsPanel";
import QueuePanel from "./QueuePanel";
import OutputLibrary from "./OutputLibrary";
import ProcessingStatus from "./ProcessingStatus";

export default function EditorLayout() {
  return (
    <>
      <ProcessingStatus /> {/* Add the status modal */}
      <div className="h-screen w-screen bg-gray-900">
        <ResizablePanelGroup direction="horizontal" className="h-full w-full">
          <ResizablePanel defaultSize={20} minSize={15}>
            <ResizablePanelGroup direction="vertical">
              <ResizablePanel defaultSize={40} minSize={20}><MediaPanel /></ResizablePanel>
              <ResizableHandle withHandle />
              <ResizablePanel defaultSize={30} minSize={20}><QueuePanel /></ResizablePanel>
              <ResizableHandle withHandle />
              <ResizablePanel defaultSize={30} minSize={20}><OutputLibrary /></ResizablePanel>
            </ResizablePanelGroup>
          </ResizablePanel>
          <ResizableHandle withHandle />
          <ResizablePanel defaultSize={55} minSize={30}><PlayerPanel /></ResizablePanel>
          <ResizableHandle withHandle />
          <ResizablePanel defaultSize={25} minSize={20}><SettingsPanel /></ResizablePanel>
        </ResizablePanelGroup>
      </div>
    </>
  );
}

```

---

<h2 id="packagesfrontendsrccomponentseditorglobalsettingspaneltsx"><code>packages/frontend/src/components/editor/GlobalSettingsPanel.tsx</code></h2>

```typescript
import { useSettingsStore, type FFmpegSettings } from '@/stores/useSettingsStore';
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Switch } from "@/components/ui/switch";
import { Slider } from "@/components/ui/slider";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";

export default function GlobalSettingsPanel() {
  const { settings, setSettings } = useSettingsStore();

  const handleSelectChange = (key: keyof FFmpegSettings) => (value: string) => {
    setSettings({ [key]: value });
  };

  return (
    <Card className="bg-transparent border-none">
      <CardHeader>
        <CardTitle>Global Settings</CardTitle>
      </CardHeader>
      <CardContent className="space-y-6">
        <div className="flex items-center justify-between">
          <Label htmlFor="combine-clips">Combine Clips into One File</Label>
          <Switch id="combine-clips" checked={settings.combineClips} onCheckedChange={(checked) => setSettings({ combineClips: checked })} />
        </div>

        <div className="space-y-2">
          <Label>Output Format</Label>
          <Select value={settings.outputFormat} onValueChange={handleSelectChange('outputFormat')}>
            <SelectTrigger><SelectValue /></SelectTrigger>
            <SelectContent>
              <SelectItem value="mp4">MP4</SelectItem>
              <SelectItem value="mov">MOV</SelectItem>
              <SelectItem value="gif">GIF</SelectItem>
            </SelectContent>
          </Select>
        </div>

        <div className="space-y-2">
          <Label>Quality (CRF) - Lower is better</Label>
          <div className="flex items-center space-x-4">
            <Slider value={[settings.quality]} onValueChange={([val]) => setSettings({ quality: val })} min={0} max={51} step={1} />
            <span className="w-10 text-center font-mono p-2 rounded-md bg-gray-900">{settings.quality}</span>
          </div>
        </div>

        <div className="space-y-2">
          <Label>Encoding Speed</Label>
          <Select value={settings.encodingSpeed} onValueChange={handleSelectChange('encodingSpeed')}>
            <SelectTrigger><SelectValue /></SelectTrigger>
            <SelectContent>
              <SelectItem value="ultrafast">Ultrafast</SelectItem>
              <SelectItem value="fast">Fast</SelectItem>
              <SelectItem value="medium">Medium</SelectItem>
              <SelectItem value="slow">Slow</SelectItem>
            </SelectContent>
          </Select>
        </div>
      </CardContent>
    </Card>
  );
}

```

---

<h2 id="packagesfrontendsrccomponentseditormediapaneltsx"><code>packages/frontend/src/components/editor/MediaPanel.tsx</code></h2>

```typescript
import { useState, useEffect, useCallback } from 'react';
import { useProjectStore } from '@/stores/useProjectStore';
import { useVideoPlayerStore } from '@/stores/useVideoPlayerStore';
import { Button } from "@/components/ui/button";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Video } from "lucide-react";
import AddVideoModal from './AddVideoModal';

export default function MediaPanel() {
  const projectName = useProjectStore((state) => state.projectName);
  const { activeVideoSource, setActiveVideo } = useVideoPlayerStore();
  
  const [videos, setVideos] = useState<string[]>([]);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const fetchVideos = useCallback(async () => {
    if (!projectName) return;
    try {
      const response = await fetch(`/api/projects/${projectName}/videos`);
      const data = await response.json();
      setVideos(data);
    } catch (error) {
      console.error("Failed to fetch videos:", error);
    }
  }, [projectName]);

  useEffect(() => {
    fetchVideos();
  }, [fetchVideos]);

  const handleVideoSelect = (videoName: string) => {
    // Construct the full URL for the video player
    const videoUrl = `/videos/${projectName}/${videoName}`;
    setActiveVideo(videoUrl);
  };
  
  const handleVideoAdded = () => {
      fetchVideos(); // Refresh the list after a video is added
  }

  return (
    <>
      <AddVideoModal 
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onVideoAdded={handleVideoAdded}
      />
      <Card className="h-full bg-gray-800 border-gray-700 rounded-none flex flex-col">
        <CardHeader>
          <CardTitle>Video Library</CardTitle>
        </CardHeader>
        <CardContent className="flex-grow flex flex-col">
          <Button onClick={() => setIsModalOpen(true)} className="w-full mb-4">
            + Add More Videos
          </Button>

          {videos.length > 0 ? (
            <ul className="space-y-2 overflow-y-auto">
              {videos.map((video) => {
                const videoUrl = `/videos/${projectName}/${video}`;
                const isSelected = activeVideoSource === videoUrl;
                return (
                  <li 
                    key={video}
                    onClick={() => handleVideoSelect(video)}
                    className={`p-2 rounded-md cursor-pointer flex items-center space-x-2 ${isSelected ? 'bg-blue-600' : 'hover:bg-gray-700'}`}
                  >
                    <Video size={16} />
                    <span className="truncate text-sm">{video}</span>
                  </li>
                );
              })}
            </ul>
          ) : (
            <div className="flex-grow flex flex-col items-center justify-center text-center text-gray-500">
              <Video size={48} className="mb-4" />
              <p>Your video library is empty.</p>
              <p className="text-sm">Click "Add More Videos" to start.</p>
            </div>
          )}
        </CardContent>
      </Card>
    </>
  );
}
```

---

<h2 id="packagesfrontendsrccomponentseditoroutputlibrarytsx"><code>packages/frontend/src/components/editor/OutputLibrary.tsx</code></h2>

```typescript
import { useState, useEffect, useCallback } from 'react';
import { useProjectStore } from '@/stores/useProjectStore';
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Download } from 'lucide-react';
import { useProcessingStore } from '@/stores/useProcessingStore';

export default function OutputLibrary() {
  const projectName = useProjectStore((state) => state.projectName);
  const isProcessing = useProcessingStore((state) => state.isProcessing);
  const [outputs, setOutputs] = useState<string[]>([]);

  const fetchOutputs = useCallback(async () => {
    if (!projectName) return;
    try {
      const response = await fetch(`/api/projects/${projectName}/outputs`);
      const data = await response.json();
      setOutputs(data);
    } catch (error) {
      console.error("Failed to fetch outputs:", error);
    }
  }, [projectName]);

  useEffect(() => {
    fetchOutputs();
  }, [fetchOutputs]);

  // Refetch when processing is no longer active (i.e., it just finished)
  useEffect(() => {
      if(!isProcessing) {
          fetchOutputs();
      }
  }, [isProcessing, fetchOutputs]);

  return (
    <Card className="h-full bg-gray-800 border-gray-700 rounded-none flex flex-col">
      <CardHeader>
        <CardTitle>Output Library</CardTitle>
      </CardHeader>
      <CardContent className="flex-grow overflow-y-auto">
        {outputs.length > 0 ? (
          <ul className="space-y-2">
            {outputs.map((video) => (
              <li key={video} className="flex items-center justify-between p-2 rounded-md bg-gray-900">
                <span className="truncate text-sm font-mono">{video}</span>
                <a href={`/videos/${projectName}/output/${video}`} download>
                  <Download size={16} className="text-blue-400 hover:text-blue-300" />
                </a>
              </li>
            ))}
          </ul>
        ) : (
          <p className="text-center text-gray-500 pt-10">No processed videos yet.</p>
        )}
      </CardContent>
    </Card>
  );
}

```

---

<h2 id="packagesfrontendsrccomponentseditorplayerpaneltsx"><code>packages/frontend/src/components/editor/PlayerPanel.tsx</code></h2>

```typescript
import { useState, useRef, useEffect } from 'react';
import ReactPlayer from 'react-player';
import { useVideoPlayerStore } from '@/stores/useVideoPlayerStore';
import { useQueueStore } from '@/stores/useQueueStore';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { formatTime } from '@/lib/utils';
import { v4 as uuidv4 } from 'uuid';

export default function PlayerPanel() {
  const { activeVideoSource } = useVideoPlayerStore();
  const addClip = useQueueStore((state) => state.addClip);
  
  const playerRef = useRef<ReactPlayer>(null);
  const [startTime, setStartTime] = useState(0);
  const [endTime, setEndTime] = useState(0);

  useEffect(() => {
    // Reset times when video source changes
    setStartTime(0);
    setEndTime(0);
  }, [activeVideoSource]);
  
  const handleDuration = (d: number) => {
    setEndTime(d); // Set initial end time to full duration
  };

  const handleAddToQueue = () => {
    if (activeVideoSource) {
      addClip({
        id: uuidv4(), // Generate a unique ID for the clip
        sourceVideo: activeVideoSource,
        startTime,
        endTime,
      });
    }
  };

  return (
    <div className="h-full w-full bg-black flex flex-col">
      <div className="flex-grow flex items-center justify-center">
        {activeVideoSource ? (
          <ReactPlayer
            ref={playerRef}
            url={activeVideoSource}
            controls={true}
            width="100%"
            height="100%"
            onDuration={handleDuration}
          />
        ) : (
          <div className="text-gray-500 text-center">
            <p className="text-lg">Select a video to begin.</p>
          </div>
        )}
      </div>

      {/* Time Controls */}
      <div className="p-4 bg-gray-900/50 space-y-4">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 items-center">
          <div className="flex items-center space-x-2">
            <Button variant="outline" size="sm" onClick={() => playerRef.current?.seekTo(startTime)}>Start</Button>
            <Input
              className="bg-gray-800 border-gray-700 font-mono text-center"
              value={formatTime(startTime)}
              readOnly
            />
            <Button variant="outline" size="sm" onClick={() => setStartTime(playerRef.current?.getCurrentTime() || 0)}>Set</Button>
          </div>
          
          <div className="flex items-center justify-center">
             <Button onClick={handleAddToQueue} disabled={!activeVideoSource}>+ Add to Queue</Button>
          </div>

          <div className="flex items-center space-x-2">
            <Button variant="outline" size="sm" onClick={() => playerRef.current?.seekTo(endTime)}>End</Button>
            <Input
              className="bg-gray-800 border-gray-700 font-mono text-center"
              value={formatTime(endTime)}
              readOnly
            />
            <Button variant="outline" size="sm" onClick={() => setEndTime(playerRef.current?.getCurrentTime() || 0)}>Set</Button>
          </div>
        </div>
      </div>
    </div>
  );
}

```

---

<h2 id="packagesfrontendsrccomponentseditorprocessingstatustsx"><code>packages/frontend/src/components/editor/ProcessingStatus.tsx</code></h2>

```typescript
import { useProcessingStore } from '@/stores/useProcessingStore';
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription } from "@/components/ui/dialog";
import { Progress } from "@/components/ui/progress";
import { Button } from '@/components/ui/button';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";

export default function ProcessingStatus() {
  const { isProcessing, progress, logs, error, outputFilePath, reset } = useProcessingStore();

  const handleClose = () => {
    if (isProcessing) return; // Don't close while processing
    reset();
  }
  
  return (
    <Dialog open={isProcessing || !!error || !!outputFilePath} onOpenChange={handleClose}>
      <DialogContent className="bg-gray-800 border-gray-700 text-white">
        <DialogHeader>
          <DialogTitle>
            {isProcessing && 'Processing Video...'}
            {!!error && 'An Error Occurred'}
            {!!outputFilePath && 'Processing Complete!'}
          </DialogTitle>
          <DialogDescription>
            {isProcessing && 'Please wait, this may take a while.'}
            {!!error && 'Something went wrong during processing.'}
            {!!outputFilePath && 'Your new video is ready.'}
          </DialogDescription>
        </DialogHeader>

        <div className="py-4">
          {isProcessing && <Progress value={progress} className="w-full" />}
          {!!error && <p className="text-red-500 bg-red-900/20 p-4 rounded-md">{error}</p>}
          {!!outputFilePath && (
            <div className="flex flex-col items-center gap-4">
              <p className="text-green-400">Successfully created your video!</p>
              <Button asChild>
                <a href={outputFilePath} download>Download Video</a>
              </Button>
            </div>
          )}
        </div>
        
        <Accordion type="single" collapsible className="w-full">
            <AccordionItem value="logs">
                <AccordionTrigger>Show Logs</AccordionTrigger>
                <AccordionContent>
                    <pre className="w-full h-48 bg-black p-2 rounded-md overflow-y-auto text-xs font-mono text-gray-400">
                        {logs.join('')}
                    </pre>
                </AccordionContent>
            </AccordionItem>
        </Accordion>
      </DialogContent>
    </Dialog>
  );
}

```

---

<h2 id="packagesfrontendsrccomponentseditorqueuepaneltsx"><code>packages/frontend/src/components/editor/QueuePanel.tsx</code></h2>

```typescript
import { useQueueStore } from '@/stores/useQueueStore';
import type { Clip } from '@/stores/useQueueStore';
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Button } from '@/components/ui/button';
import { DndContext, closestCenter } from '@dnd-kit/core';
import type { DragEndEvent } from '@dnd-kit/core';
import { SortableContext, useSortable, verticalListSortingStrategy } from '@dnd-kit/sortable';
import { CSS } from '@dnd-kit/utilities';
import { GripVertical, Trash2 } from 'lucide-react';
import { formatTime } from '@/lib/utils';

// Component for a single item in the queue
function SortableClipItem({ clip }: { clip: Clip }) {
  const removeClip = useQueueStore((state) => state.removeClip);
  const { attributes, listeners, setNodeRef, transform, transition } = useSortable({ id: clip.id });

  const style = {
    transform: CSS.Transform.toString(transform),
    transition,
  };

  return (
    <div ref={setNodeRef} style={style} className="flex items-center bg-gray-900 p-2 rounded-md space-x-2">
      <div {...attributes} {...listeners} className="cursor-grab p-1">
        <GripVertical size={16} />
      </div>
      <div className="flex-grow truncate text-sm">
        <p className="font-mono truncate">{clip.sourceVideo.split('/').pop()}</p>
        <p className="text-xs text-gray-400">
          {formatTime(clip.startTime)} → {formatTime(clip.endTime)}
        </p>
      </div>
      <Button variant="ghost" size="icon" onClick={() => removeClip(clip.id)}>
        <Trash2 size={16} className="text-red-500" />
      </Button>
    </div>
  );
}

// Main Panel Component
export default function QueuePanel() {
  const { queue, reorderQueue } = useQueueStore();

  const handleDragEnd = (event: DragEndEvent) => {
    const { active, over } = event;
    if (over && active.id !== over.id) {
      const oldIndex = queue.findIndex((c) => c.id === active.id);
      const newIndex = queue.findIndex((c) => c.id === over.id);
      const newQueue = [...queue];
      const [movedItem] = newQueue.splice(oldIndex, 1);
      newQueue.splice(newIndex, 0, movedItem); // Correctly insert at newIndex
      reorderQueue(newQueue);
    }
  };

  return (
    <Card className="h-full bg-gray-800 border-gray-700 rounded-none flex flex-col">
      <CardHeader>
        <CardTitle>Trim Queue</CardTitle>
      </CardHeader>
      <CardContent className="flex-grow overflow-y-auto">
        {queue.length > 0 ? (
          <DndContext collisionDetection={closestCenter} onDragEnd={handleDragEnd}>
            <SortableContext items={queue.map(c => c.id)} strategy={verticalListSortingStrategy}>
              <div className="space-y-2">
                {queue.map(clip => <SortableClipItem key={clip.id} clip={clip} />)}
              </div>
            </SortableContext>
          </DndContext>
        ) : (
          <div className="text-center text-gray-500 pt-10">
            <p>Your queue is empty.</p>
            <p className="text-sm">Set start/end times on a video and click "Add to Queue".</p>
          </div>
        )}
      </CardContent>
    </Card>
  );
}

```

---

<h2 id="packagesfrontendsrccomponentseditorsettingspaneltsx"><code>packages/frontend/src/components/editor/SettingsPanel.tsx</code></h2>

```typescript
import GlobalSettingsPanel from "./GlobalSettingsPanel";
import { Button } from "@/components/ui/button";
import { useQueueStore } from "@/stores/useQueueStore";
import { useSettingsStore } from "@/stores/useSettingsStore";
import { useProjectStore } from "@/stores/useProjectStore";
import { useProcessingStore } from "@/stores/useProcessingStore";
import { socket } from "@/lib/socket";

export default function SettingsPanel() {
    const queue = useQueueStore((state) => state.queue);
    const settings = useSettingsStore((state) => state.settings);
    const projectName = useProjectStore((state) => state.projectName);
    const { isProcessing, startProcessing } = useProcessingStore();

    const handleProcessClips = () => {
        if (!projectName || queue.length === 0 || isProcessing) return;

        startProcessing(); // Update UI state to show processing modal

        // Send data to backend via Socket.IO
        socket.emit('start-processing', {
            queue,
            settings,
            projectName,
        });
    };

    return (
        <div className="h-full flex flex-col bg-gray-800">
            <div className="flex-grow overflow-y-auto">
                <GlobalSettingsPanel />
            </div>
            <div className="p-4 border-t border-gray-700 space-y-2">
                <Button 
                    onClick={handleProcessClips} 
                    className="w-full" 
                    size="lg"
                    disabled={isProcessing || queue.length === 0}
                >
                    {isProcessing ? 'Processing...' : 'Process Clips'}
                </Button>
            </div>
        </div>
    );
}

```

---

<h2 id="packagesfrontendsrccomponentsuiaccordiontsx"><code>packages/frontend/src/components/ui/accordion.tsx</code></h2>

```typescript
import * as React from "react"
import * as AccordionPrimitive from "@radix-ui/react-accordion"
import { ChevronDownIcon } from "lucide-react"

import { cn } from "@/lib/utils"

function Accordion({
  ...props
}: React.ComponentProps<typeof AccordionPrimitive.Root>) {
  return <AccordionPrimitive.Root data-slot="accordion" {...props} />
}

function AccordionItem({
  className,
  ...props
}: React.ComponentProps<typeof AccordionPrimitive.Item>) {
  return (
    <AccordionPrimitive.Item
      data-slot="accordion-item"
      className={cn("border-b last:border-b-0", className)}
      {...props}
    />
  )
}

function AccordionTrigger({
  className,
  children,
  ...props
}: React.ComponentProps<typeof AccordionPrimitive.Trigger>) {
  return (
    <AccordionPrimitive.Header className="flex">
      <AccordionPrimitive.Trigger
        data-slot="accordion-trigger"
        className={cn(
          "focus-visible:border-ring focus-visible:ring-ring/50 flex flex-1 items-start justify-between gap-4 rounded-md py-4 text-left text-sm font-medium transition-all outline-none hover:underline focus-visible:ring-[3px] disabled:pointer-events-none disabled:opacity-50 [&[data-state=open]>svg]:rotate-180",
          className
        )}
        {...props}
      >
        {children}
        <ChevronDownIcon className="text-muted-foreground pointer-events-none size-4 shrink-0 translate-y-0.5 transition-transform duration-200" />
      </AccordionPrimitive.Trigger>
    </AccordionPrimitive.Header>
  )
}

function AccordionContent({
  className,
  children,
  ...props
}: React.ComponentProps<typeof AccordionPrimitive.Content>) {
  return (
    <AccordionPrimitive.Content
      data-slot="accordion-content"
      className="data-[state=closed]:animate-accordion-up data-[state=open]:animate-accordion-down overflow-hidden text-sm"
      {...props}
    >
      <div className={cn("pt-0 pb-4", className)}>{children}</div>
    </AccordionPrimitive.Content>
  )
}

export { Accordion, AccordionItem, AccordionTrigger, AccordionContent }

```

---

<h2 id="packagesfrontendsrccomponentsuibuttontsx"><code>packages/frontend/src/components/ui/button.tsx</code></h2>

```typescript
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { buttonVariants } from "./variants";
import { type VariantProps } from "class-variance-authority";

import { cn } from "@/lib/utils"

function Button({
  className,
  variant,
  size,
  asChild = false,
  ...props
}: React.ComponentProps<"button"> &
  VariantProps<typeof buttonVariants> & {
    asChild?: boolean
  }) {
  const Comp = asChild ? Slot : "button"

  return (
    <Comp
      data-slot="button"
      className={cn(buttonVariants({ variant, size, className }))}
      {...props}
    />
  )
}

export { Button }

```

---

<h2 id="packagesfrontendsrccomponentsuicardtsx"><code>packages/frontend/src/components/ui/card.tsx</code></h2>

```typescript
import * as React from "react"

import { cn } from "@/lib/utils"

function Card({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card"
      className={cn(
        "bg-card text-card-foreground flex flex-col gap-6 rounded-xl border py-6 shadow-sm",
        className
      )}
      {...props}
    />
  )
}

function CardHeader({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-header"
      className={cn(
        "@container/card-header grid auto-rows-min grid-rows-[auto_auto] items-start gap-1.5 px-6 has-data-[slot=card-action]:grid-cols-[1fr_auto] [.border-b]:pb-6",
        className
      )}
      {...props}
    />
  )
}

function CardTitle({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-title"
      className={cn("leading-none font-semibold", className)}
      {...props}
    />
  )
}

function CardDescription({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-description"
      className={cn("text-muted-foreground text-sm", className)}
      {...props}
    />
  )
}

function CardAction({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-action"
      className={cn(
        "col-start-2 row-span-2 row-start-1 self-start justify-self-end",
        className
      )}
      {...props}
    />
  )
}

function CardContent({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-content"
      className={cn("px-6", className)}
      {...props}
    />
  )
}

function CardFooter({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-footer"
      className={cn("flex items-center px-6 [.border-t]:pt-6", className)}
      {...props}
    />
  )
}

export {
  Card,
  CardHeader,
  CardFooter,
  CardTitle,
  CardAction,
  CardDescription,
  CardContent,
}

```

---

<h2 id="packagesfrontendsrccomponentsuidialogtsx"><code>packages/frontend/src/components/ui/dialog.tsx</code></h2>

```typescript
import * as React from "react"
import * as DialogPrimitive from "@radix-ui/react-dialog"
import { XIcon } from "lucide-react"

import { cn } from "@/lib/utils"

function Dialog({
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Root>) {
  return <DialogPrimitive.Root data-slot="dialog" {...props} />
}

function DialogTrigger({
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Trigger>) {
  return <DialogPrimitive.Trigger data-slot="dialog-trigger" {...props} />
}

function DialogPortal({
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Portal>) {
  return <DialogPrimitive.Portal data-slot="dialog-portal" {...props} />
}

function DialogClose({
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Close>) {
  return <DialogPrimitive.Close data-slot="dialog-close" {...props} />
}

function DialogOverlay({
  className,
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Overlay>) {
  return (
    <DialogPrimitive.Overlay
      data-slot="dialog-overlay"
      className={cn(
        "data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 fixed inset-0 z-50 bg-black/50",
        className
      )}
      {...props}
    />
  )
}

function DialogContent({
  className,
  children,
  showCloseButton = true,
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Content> & {
  showCloseButton?: boolean
}) {
  return (
    <DialogPortal data-slot="dialog-portal">
      <DialogOverlay />
      <DialogPrimitive.Content
        data-slot="dialog-content"
        className={cn(
          "bg-background data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 fixed top-[50%] left-[50%] z-50 grid w-full max-w-[calc(100%-2rem)] translate-x-[-50%] translate-y-[-50%] gap-4 rounded-lg border p-6 shadow-lg duration-200 sm:max-w-lg",
          className
        )}
        {...props}
      >
        {children}
        {showCloseButton && (
          <DialogPrimitive.Close
            data-slot="dialog-close"
            className="ring-offset-background focus:ring-ring data-[state=open]:bg-accent data-[state=open]:text-muted-foreground absolute top-4 right-4 rounded-xs opacity-70 transition-opacity hover:opacity-100 focus:ring-2 focus:ring-offset-2 focus:outline-hidden disabled:pointer-events-none [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4"
          >
            <XIcon />
            <span className="sr-only">Close</span>
          </DialogPrimitive.Close>
        )}
      </DialogPrimitive.Content>
    </DialogPortal>
  )
}

function DialogHeader({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="dialog-header"
      className={cn("flex flex-col gap-2 text-center sm:text-left", className)}
      {...props}
    />
  )
}

function DialogFooter({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="dialog-footer"
      className={cn(
        "flex flex-col-reverse gap-2 sm:flex-row sm:justify-end",
        className
      )}
      {...props}
    />
  )
}

function DialogTitle({
  className,
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Title>) {
  return (
    <DialogPrimitive.Title
      data-slot="dialog-title"
      className={cn("text-lg leading-none font-semibold", className)}
      {...props}
    />
  )
}

function DialogDescription({
  className,
  ...props
}: React.ComponentProps<typeof DialogPrimitive.Description>) {
  return (
    <DialogPrimitive.Description
      data-slot="dialog-description"
      className={cn("text-muted-foreground text-sm", className)}
      {...props}
    />
  )
}

export {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogOverlay,
  DialogPortal,
  DialogTitle,
  DialogTrigger,
}

```

---

<h2 id="packagesfrontendsrccomponentsuiinputtsx"><code>packages/frontend/src/components/ui/input.tsx</code></h2>

```typescript
import * as React from "react"

import { cn } from "@/lib/utils"

function Input({ className, type, ...props }: React.ComponentProps<"input">) {
  return (
    <input
      type={type}
      data-slot="input"
      className={cn(
        "file:text-foreground placeholder:text-muted-foreground selection:bg-primary selection:text-primary-foreground dark:bg-input/30 border-input flex h-9 w-full min-w-0 rounded-md border bg-transparent px-3 py-1 text-base shadow-xs transition-[color,box-shadow] outline-none file:inline-flex file:h-7 file:border-0 file:bg-transparent file:text-sm file:font-medium disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
        "focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px]",
        "aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive",
        className
      )}
      {...props}
    />
  )
}

export { Input }

```

---

<h2 id="packagesfrontendsrccomponentsuilabeltsx"><code>packages/frontend/src/components/ui/label.tsx</code></h2>

```typescript
import * as React from "react"
import * as LabelPrimitive from "@radix-ui/react-label"

import { cn } from "@/lib/utils"

function Label({
  className,
  ...props
}: React.ComponentProps<typeof LabelPrimitive.Root>) {
  return (
    <LabelPrimitive.Root
      data-slot="label"
      className={cn(
        "flex items-center gap-2 text-sm leading-none font-medium select-none group-data-[disabled=true]:pointer-events-none group-data-[disabled=true]:opacity-50 peer-disabled:cursor-not-allowed peer-disabled:opacity-50",
        className
      )}
      {...props}
    />
  )
}

export { Label }

```

---

<h2 id="packagesfrontendsrccomponentsuiprogresstsx"><code>packages/frontend/src/components/ui/progress.tsx</code></h2>

```typescript
"use client"

import * as React from "react"
import * as ProgressPrimitive from "@radix-ui/react-progress"

import { cn } from "@/lib/utils"

function Progress({
  className,
  value,
  ...props
}: React.ComponentProps<typeof ProgressPrimitive.Root>) {
  return (
    <ProgressPrimitive.Root
      data-slot="progress"
      className={cn(
        "bg-primary/20 relative h-2 w-full overflow-hidden rounded-full",
        className
      )}
      {...props}
    >
      <ProgressPrimitive.Indicator
        data-slot="progress-indicator"
        className="bg-primary h-full w-full flex-1 transition-all"
        style={{ transform: `translateX(-${100 - (value || 0)}%)` }}
      />
    </ProgressPrimitive.Root>
  )
}

export { Progress }

```

---

<h2 id="packagesfrontendsrccomponentsuiresizabletsx"><code>packages/frontend/src/components/ui/resizable.tsx</code></h2>

```typescript
import * as React from "react"
import { GripVerticalIcon } from "lucide-react"
import * as ResizablePrimitive from "react-resizable-panels"

import { cn } from "@/lib/utils"

function ResizablePanelGroup({
  className,
  ...props
}: React.ComponentProps<typeof ResizablePrimitive.PanelGroup>) {
  return (
    <ResizablePrimitive.PanelGroup
      data-slot="resizable-panel-group"
      className={cn(
        "flex h-full w-full data-[panel-group-direction=vertical]:flex-col",
        className
      )}
      {...props}
    />
  )
}

function ResizablePanel({
  ...props
}: React.ComponentProps<typeof ResizablePrimitive.Panel>) {
  return <ResizablePrimitive.Panel data-slot="resizable-panel" {...props} />
}

function ResizableHandle({
  withHandle,
  className,
  ...props
}: React.ComponentProps<typeof ResizablePrimitive.PanelResizeHandle> & {
  withHandle?: boolean
}) {
  return (
    <ResizablePrimitive.PanelResizeHandle
      data-slot="resizable-handle"
      className={cn(
        "bg-border focus-visible:ring-ring relative flex w-px items-center justify-center after:absolute after:inset-y-0 after:left-1/2 after:w-1 after:-translate-x-1/2 focus-visible:ring-1 focus-visible:ring-offset-1 focus-visible:outline-hidden data-[panel-group-direction=vertical]:h-px data-[panel-group-direction=vertical]:w-full data-[panel-group-direction=vertical]:after:left-0 data-[panel-group-direction=vertical]:after:h-1 data-[panel-group-direction=vertical]:after:w-full data-[panel-group-direction=vertical]:after:translate-x-0 data-[panel-group-direction=vertical]:after:-translate-y-1/2 [&[data-panel-group-direction=vertical]>div]:rotate-90",
        className
      )}
      {...props}
    >
      {withHandle && (
        <div className="bg-border z-10 flex h-4 w-3 items-center justify-center rounded-xs border">
          <GripVerticalIcon className="size-2.5" />
        </div>
      )}
    </ResizablePrimitive.PanelResizeHandle>
  )
}

export { ResizablePanelGroup, ResizablePanel, ResizableHandle }

```

---

<h2 id="packagesfrontendsrccomponentsuiselecttsx"><code>packages/frontend/src/components/ui/select.tsx</code></h2>

```typescript
"use client"

import * as React from "react"
import * as SelectPrimitive from "@radix-ui/react-select"
import { CheckIcon, ChevronDownIcon, ChevronUpIcon } from "lucide-react"

import { cn } from "@/lib/utils"

function Select({
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Root>) {
  return <SelectPrimitive.Root data-slot="select" {...props} />
}

function SelectGroup({
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Group>) {
  return <SelectPrimitive.Group data-slot="select-group" {...props} />
}

function SelectValue({
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Value>) {
  return <SelectPrimitive.Value data-slot="select-value" {...props} />
}

function SelectTrigger({
  className,
  size = "default",
  children,
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Trigger> & {
  size?: "sm" | "default"
}) {
  return (
    <SelectPrimitive.Trigger
      data-slot="select-trigger"
      data-size={size}
      className={cn(
        "border-input data-[placeholder]:text-muted-foreground [&_svg:not([class*='text-'])]:text-muted-foreground focus-visible:border-ring focus-visible:ring-ring/50 aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive dark:bg-input/30 dark:hover:bg-input/50 flex w-fit items-center justify-between gap-2 rounded-md border bg-transparent px-3 py-2 text-sm whitespace-nowrap shadow-xs transition-[color,box-shadow] outline-none focus-visible:ring-[3px] disabled:cursor-not-allowed disabled:opacity-50 data-[size=default]:h-9 data-[size=sm]:h-8 *:data-[slot=select-value]:line-clamp-1 *:data-[slot=select-value]:flex *:data-[slot=select-value]:items-center *:data-[slot=select-value]:gap-2 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        className
      )}
      {...props}
    >
      {children}
      <SelectPrimitive.Icon asChild>
        <ChevronDownIcon className="size-4 opacity-50" />
      </SelectPrimitive.Icon>
    </SelectPrimitive.Trigger>
  )
}

function SelectContent({
  className,
  children,
  position = "popper",
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Content>) {
  return (
    <SelectPrimitive.Portal>
      <SelectPrimitive.Content
        data-slot="select-content"
        className={cn(
          "bg-popover text-popover-foreground data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 relative z-50 max-h-(--radix-select-content-available-height) min-w-[8rem] origin-(--radix-select-content-transform-origin) overflow-x-hidden overflow-y-auto rounded-md border shadow-md",
          position === "popper" &&
            "data-[side=bottom]:translate-y-1 data-[side=left]:-translate-x-1 data-[side=right]:translate-x-1 data-[side=top]:-translate-y-1",
          className
        )}
        position={position}
        {...props}
      >
        <SelectScrollUpButton />
        <SelectPrimitive.Viewport
          className={cn(
            "p-1",
            position === "popper" &&
              "h-[var(--radix-select-trigger-height)] w-full min-w-[var(--radix-select-trigger-width)] scroll-my-1"
          )}
        >
          {children}
        </SelectPrimitive.Viewport>
        <SelectScrollDownButton />
      </SelectPrimitive.Content>
    </SelectPrimitive.Portal>
  )
}

function SelectLabel({
  className,
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Label>) {
  return (
    <SelectPrimitive.Label
      data-slot="select-label"
      className={cn("text-muted-foreground px-2 py-1.5 text-xs", className)}
      {...props}
    />
  )
}

function SelectItem({
  className,
  children,
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Item>) {
  return (
    <SelectPrimitive.Item
      data-slot="select-item"
      className={cn(
        "focus:bg-accent focus:text-accent-foreground [&_svg:not([class*='text-'])]:text-muted-foreground relative flex w-full cursor-default items-center gap-2 rounded-sm py-1.5 pr-8 pl-2 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4 *:[span]:last:flex *:[span]:last:items-center *:[span]:last:gap-2",
        className
      )}
      {...props}
    >
      <span className="absolute right-2 flex size-3.5 items-center justify-center">
        <SelectPrimitive.ItemIndicator>
          <CheckIcon className="size-4" />
        </SelectPrimitive.ItemIndicator>
      </span>
      <SelectPrimitive.ItemText>{children}</SelectPrimitive.ItemText>
    </SelectPrimitive.Item>
  )
}

function SelectSeparator({
  className,
  ...props
}: React.ComponentProps<typeof SelectPrimitive.Separator>) {
  return (
    <SelectPrimitive.Separator
      data-slot="select-separator"
      className={cn("bg-border pointer-events-none -mx-1 my-1 h-px", className)}
      {...props}
    />
  )
}

function SelectScrollUpButton({
  className,
  ...props
}: React.ComponentProps<typeof SelectPrimitive.ScrollUpButton>) {
  return (
    <SelectPrimitive.ScrollUpButton
      data-slot="select-scroll-up-button"
      className={cn(
        "flex cursor-default items-center justify-center py-1",
        className
      )}
      {...props}
    >
      <ChevronUpIcon className="size-4" />
    </SelectPrimitive.ScrollUpButton>
  )
}

function SelectScrollDownButton({
  className,
  ...props
}: React.ComponentProps<typeof SelectPrimitive.ScrollDownButton>) {
  return (
    <SelectPrimitive.ScrollDownButton
      data-slot="select-scroll-down-button"
      className={cn(
        "flex cursor-default items-center justify-center py-1",
        className
      )}
      {...props}
    >
      <ChevronDownIcon className="size-4" />
    </SelectPrimitive.ScrollDownButton>
  )
}

export {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectScrollDownButton,
  SelectScrollUpButton,
  SelectSeparator,
  SelectTrigger,
  SelectValue,
}

```

---

<h2 id="packagesfrontendsrccomponentsuislidertsx"><code>packages/frontend/src/components/ui/slider.tsx</code></h2>

```typescript
import * as React from "react"
import * as SliderPrimitive from "@radix-ui/react-slider"

import { cn } from "@/lib/utils"

function Slider({
  className,
  defaultValue,
  value,
  min = 0,
  max = 100,
  ...props
}: React.ComponentProps<typeof SliderPrimitive.Root>) {
  const _values = React.useMemo(
    () =>
      Array.isArray(value)
        ? value
        : Array.isArray(defaultValue)
          ? defaultValue
          : [min, max],
    [value, defaultValue, min, max]
  )

  return (
    <SliderPrimitive.Root
      data-slot="slider"
      defaultValue={defaultValue}
      value={value}
      min={min}
      max={max}
      className={cn(
        "relative flex w-full touch-none items-center select-none data-[disabled]:opacity-50 data-[orientation=vertical]:h-full data-[orientation=vertical]:min-h-44 data-[orientation=vertical]:w-auto data-[orientation=vertical]:flex-col",
        className
      )}
      {...props}
    >
      <SliderPrimitive.Track
        data-slot="slider-track"
        className={cn(
          "bg-muted relative grow overflow-hidden rounded-full data-[orientation=horizontal]:h-1.5 data-[orientation=horizontal]:w-full data-[orientation=vertical]:h-full data-[orientation=vertical]:w-1.5"
        )}
      >
        <SliderPrimitive.Range
          data-slot="slider-range"
          className={cn(
            "bg-primary absolute data-[orientation=horizontal]:h-full data-[orientation=vertical]:w-full"
          )}
        />
      </SliderPrimitive.Track>
      {Array.from({ length: _values.length }, (_, index) => (
        <SliderPrimitive.Thumb
          data-slot="slider-thumb"
          key={index}
          className="border-primary bg-background ring-ring/50 block size-4 shrink-0 rounded-full border shadow-sm transition-[color,box-shadow] hover:ring-4 focus-visible:ring-4 focus-visible:outline-hidden disabled:pointer-events-none disabled:opacity-50"
        />
      ))}
    </SliderPrimitive.Root>
  )
}

export { Slider }

```

---

<h2 id="packagesfrontendsrccomponentsuiswitchtsx"><code>packages/frontend/src/components/ui/switch.tsx</code></h2>

```typescript
"use client"

import * as React from "react"
import * as SwitchPrimitive from "@radix-ui/react-switch"

import { cn } from "@/lib/utils"

function Switch({
  className,
  ...props
}: React.ComponentProps<typeof SwitchPrimitive.Root>) {
  return (
    <SwitchPrimitive.Root
      data-slot="switch"
      className={cn(
        "peer data-[state=checked]:bg-primary data-[state=unchecked]:bg-input focus-visible:border-ring focus-visible:ring-ring/50 dark:data-[state=unchecked]:bg-input/80 inline-flex h-[1.15rem] w-8 shrink-0 items-center rounded-full border border-transparent shadow-xs transition-all outline-none focus-visible:ring-[3px] disabled:cursor-not-allowed disabled:opacity-50",
        className
      )}
      {...props}
    >
      <SwitchPrimitive.Thumb
        data-slot="switch-thumb"
        className={cn(
          "bg-background dark:data-[state=unchecked]:bg-foreground dark:data-[state=checked]:bg-primary-foreground pointer-events-none block size-4 rounded-full ring-0 transition-transform data-[state=checked]:translate-x-[calc(100%-2px)] data-[state=unchecked]:translate-x-0"
        )}
      />
    </SwitchPrimitive.Root>
  )
}

export { Switch }

```

---

<h2 id="packagesfrontendsrccomponentsuitabstsx"><code>packages/frontend/src/components/ui/tabs.tsx</code></h2>

```typescript
"use client"

import * as React from "react"
import * as TabsPrimitive from "@radix-ui/react-tabs"

import { cn } from "@/lib/utils"

function Tabs({
  className,
  ...props
}: React.ComponentProps<typeof TabsPrimitive.Root>) {
  return (
    <TabsPrimitive.Root
      data-slot="tabs"
      className={cn("flex flex-col gap-2", className)}
      {...props}
    />
  )
}

function TabsList({
  className,
  ...props
}: React.ComponentProps<typeof TabsPrimitive.List>) {
  return (
    <TabsPrimitive.List
      data-slot="tabs-list"
      className={cn(
        "bg-muted text-muted-foreground inline-flex h-9 w-fit items-center justify-center rounded-lg p-[3px]",
        className
      )}
      {...props}
    />
  )
}

function TabsTrigger({
  className,
  ...props
}: React.ComponentProps<typeof TabsPrimitive.Trigger>) {
  return (
    <TabsPrimitive.Trigger
      data-slot="tabs-trigger"
      className={cn(
        "data-[state=active]:bg-background dark:data-[state=active]:text-foreground focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:outline-ring dark:data-[state=active]:border-input dark:data-[state=active]:bg-input/30 text-foreground dark:text-muted-foreground inline-flex h-[calc(100%-1px)] flex-1 items-center justify-center gap-1.5 rounded-md border border-transparent px-2 py-1 text-sm font-medium whitespace-nowrap transition-[color,box-shadow] focus-visible:ring-[3px] focus-visible:outline-1 disabled:pointer-events-none disabled:opacity-50 data-[state=active]:shadow-sm [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        className
      )}
      {...props}
    />
  )
}

function TabsContent({
  className,
  ...props
}: React.ComponentProps<typeof TabsPrimitive.Content>) {
  return (
    <TabsPrimitive.Content
      data-slot="tabs-content"
      className={cn("flex-1 outline-none", className)}
      {...props}
    />
  )
}

export { Tabs, TabsList, TabsTrigger, TabsContent }

```

---

<h2 id="packagesfrontendsrccomponentsuivariantsts"><code>packages/frontend/src/components/ui/variants.ts</code></h2>

```typescript
import { cva } from "class-variance-authority";

export const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive",
  {
    variants: {
      variant: {
        default:
          "bg-primary text-primary-foreground shadow-xs hover:bg-primary/90",
        destructive:
          "bg-destructive text-white shadow-xs hover:bg-destructive/90 focus-visible:ring-destructive/20 dark:focus-visible:ring-destructive/40 dark:bg-destructive/60",
        outline:
          "border bg-background shadow-xs hover:bg-accent hover:text-accent-foreground dark:bg-input/30 dark:border-input dark:hover:bg-input/50",
        secondary:
          "bg-secondary text-secondary-foreground shadow-xs hover:bg-secondary/80",
        ghost:
          "hover:bg-accent hover:text-accent-foreground dark:hover:bg-accent/50",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-9 px-4 py-2 has-[>svg]:px-3",
        sm: "h-8 rounded-md gap-1.5 px-3 has-[>svg]:px-2.5",
        lg: "h-10 rounded-md px-6 has-[>svg]:px-4",
        icon: "size-9",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
);

```

---

<h2 id="packagesfrontendsrcindexcss"><code>packages/frontend/src/index.css</code></h2>

```css

@import "tw-animate-css";

@custom-variant dark (&:is(.dark *));

@tailwind base;
@tailwind components;
@tailwind utilities;

@theme inline {
  --radius-sm: calc(var(--radius) - 4px);
  --radius-md: calc(var(--radius) - 2px);
  --radius-lg: var(--radius);
  --radius-xl: calc(var(--radius) + 4px);
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-card: var(--card);
  --color-card-foreground: var(--card-foreground);
  --color-popover: var(--popover);
  --color-popover-foreground: var(--popover-foreground);
  --color-primary: var(--primary);
  --color-primary-foreground: var(--primary-foreground);
  --color-secondary: var(--secondary);
  --color-secondary-foreground: var(--secondary-foreground);
  --color-muted: var(--muted);
  --color-muted-foreground: var(--muted-foreground);
  --color-accent: var(--accent);
  --color-accent-foreground: var(--accent-foreground);
  --color-destructive: var(--destructive);
  --color-border: var(--border);
  --color-input: var(--input);
  --color-ring: var(--ring);
  --color-chart-1: var(--chart-1);
  --color-chart-2: var(--chart-2);
  --color-chart-3: var(--chart-3);
  --color-chart-4: var(--chart-4);
  --color-chart-5: var(--chart-5);
  --color-sidebar: var(--sidebar);
  --color-sidebar-foreground: var(--sidebar-foreground);
  --color-sidebar-primary: var(--sidebar-primary);
  --color-sidebar-primary-foreground: var(--sidebar-primary-foreground);
  --color-sidebar-accent: var(--sidebar-accent);
  --color-sidebar-accent-foreground: var(--sidebar-accent-foreground);
  --color-sidebar-border: var(--sidebar-border);
  --color-sidebar-ring: var(--sidebar-ring);
}

:root {
  --radius: 0.625rem;
  --background: oklch(1 0 0);
  --foreground: oklch(0.145 0 0);
  --card: oklch(1 0 0);
  --card-foreground: oklch(0.145 0 0);
  --popover: oklch(1 0 0);
  --popover-foreground: oklch(0.145 0 0);
  --primary: oklch(0.205 0 0);
  --primary-foreground: oklch(0.985 0 0);
  --secondary: oklch(0.97 0 0);
  --secondary-foreground: oklch(0.205 0 0);
  --muted: oklch(0.97 0 0);
  --muted-foreground: oklch(0.556 0 0);
  --accent: oklch(0.97 0 0);
  --accent-foreground: oklch(0.205 0 0);
  --destructive: oklch(0.577 0.245 27.325);
  --border: oklch(0.922 0 0);
  --input: oklch(0.922 0 0);
  --ring: oklch(0.708 0 0);
  --chart-1: oklch(0.646 0.222 41.116);
  --chart-2: oklch(0.6 0.118 184.704);
  --chart-3: oklch(0.398 0.07 227.392);
  --chart-4: oklch(0.828 0.189 84.429);
  --chart-5: oklch(0.769 0.188 70.08);
  --sidebar: oklch(0.985 0 0);
  --sidebar-foreground: oklch(0.145 0 0);
  --sidebar-primary: oklch(0.205 0 0);
  --sidebar-primary-foreground: oklch(0.985 0 0);
  --sidebar-accent: oklch(0.97 0 0);
  --sidebar-accent-foreground: oklch(0.205 0 0);
  --sidebar-border: oklch(0.922 0 0);
  --sidebar-ring: oklch(0.708 0 0);
}

.dark {
  --background: oklch(0.145 0 0);
  --foreground: oklch(0.985 0 0);
  --card: oklch(0.205 0 0);
  --card-foreground: oklch(0.985 0 0);
  --popover: oklch(0.205 0 0);
  --popover-foreground: oklch(0.985 0 0);
  --primary: oklch(0.922 0 0);
  --primary-foreground: oklch(0.205 0 0);
  --secondary: oklch(0.269 0 0);
  --secondary-foreground: oklch(0.985 0 0);
  --muted: oklch(0.269 0 0);
  --muted-foreground: oklch(0.708 0 0);
  --accent: oklch(0.269 0 0);
  --accent-foreground: oklch(0.985 0 0);
  --destructive: oklch(0.704 0.191 22.216);
  --border: oklch(1 0 0 / 10%);
  --input: oklch(1 0 0 / 15%);
  --ring: oklch(0.556 0 0);
  --chart-1: oklch(0.488 0.243 264.376);
  --chart-2: oklch(0.696 0.17 162.48);
  --chart-3: oklch(0.769 0.188 70.08);
  --chart-4: oklch(0.627 0.265 303.9);
  --chart-5: oklch(0.645 0.246 16.439);
  --sidebar: oklch(0.205 0 0);
  --sidebar-foreground: oklch(0.985 0 0);
  --sidebar-primary: oklch(0.488 0.243 264.376);
  --sidebar-primary-foreground: oklch(0.985 0 0);
  --sidebar-accent: oklch(0.269 0 0);
  --sidebar-accent-foreground: oklch(0.985 0 0);
  --sidebar-border: oklch(1 0 0 / 10%);
  --sidebar-ring: oklch(0.556 0 0);
}

@layer base {
  * {
    @apply border-border outline-ring/50;
  }
  body {
    @apply bg-background text-foreground;
  }
}
```

---

<h2 id="packagesfrontendsrclibsocketts"><code>packages/frontend/src/lib/socket.ts</code></h2>

```typescript
import { io } from 'socket.io-client';

const URL = 'http://localhost:5001'; // Your backend URL
export const socket = io(URL, {
  autoConnect: false // We will connect manually
});

```

---

<h2 id="packagesfrontendsrclibutilsts"><code>packages/frontend/src/lib/utils.ts</code></h2>

```typescript
import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

// Add this new function to the file
export function formatTime(seconds: number): string {
  if (isNaN(seconds) || seconds < 0) {
    return '00:00:00.000';
  }

  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);
  const secs = Math.floor(seconds % 60);
  const ms = Math.floor((seconds - Math.floor(seconds)) * 1000);

  return `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(secs).padStart(2, '0')}.${String(ms).padStart(3, '0')}`;
}

```

---

<h2 id="packagesfrontendsrcmaintsx"><code>packages/frontend/src/main.tsx</code></h2>

```typescript
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)

```

---

<h2 id="packagesfrontendsrcpagesdashboardpagetsx"><code>packages/frontend/src/pages/DashboardPage.tsx</code></h2>

```typescript
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";

export default function DashboardPage() {
  const [projects, setProjects] = useState<string[]>([]);
  const [newProjectName, setNewProjectName] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  // Fetch existing projects from the backend
  const fetchProjects = async () => {
    try {
      const response = await fetch('/api/projects');
      if (!response.ok) throw new Error('Network response was not ok');
      const data = await response.json();
      setProjects(data);
    } catch (err) {
      setError('Failed to fetch projects.');
    }
  };

  useEffect(() => {
    fetchProjects();
  }, []);

  // Handle creating a new project
  const handleCreateProject = async (e: React.FormEvent) => {
    e.preventDefault(); // Prevent form submission from reloading the page
    setError('');
    if (!newProjectName) {
      setError('Project name cannot be empty.');
      return;
    }

    try {
      const response = await fetch('/api/projects', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ projectName: newProjectName }),
      });
      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.message || 'Failed to create project.');
      }
      
      handleOpenProject(data.projectName); // Open the new project immediately

    } catch (err: any) {
      setError(err.message);
    }
  };
  
  // Navigate to the editor for a specific project
  const handleOpenProject = (projectName: string) => {
    navigate(`/editor/${projectName}`);
  };

  return (
    <div className="container mx-auto p-4 sm:p-8">
      <header className="mb-12 text-center">
        <h1 className="text-5xl font-bold tracking-tight mb-2">Veditor</h1>
        <p className="text-muted-foreground">Your Modern Video Editor</p>
      </header>

      <main className="max-w-2xl mx-auto space-y-10">
        {/* Create New Project Section */}
        <Card>
          <CardHeader>
            <CardTitle>Create New Project</CardTitle>
            <CardDescription>Use lowercase letters, numbers, and hyphens only.</CardDescription>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleCreateProject} className="flex w-full items-center space-x-2">
              <Input
                type="text"
                placeholder="e.g., summer-vacation-2025"
                value={newProjectName}
                onChange={(e) => setNewProjectName(e.target.value)}
              />
              <Button type="submit">Create and Open</Button>
            </form>
            {error && <p className="text-destructive text-sm mt-2">{error}</p>}
          </CardContent>
        </Card>

        {/* Existing Projects Section */}
        <Card>
          <CardHeader>
            <CardTitle>Existing Projects</CardTitle>
          </CardHeader>
          <CardContent>
            {projects.length > 0 ? (
              <ul className="space-y-2">
                {projects.map((project) => (
                  <li key={project} className="flex items-center justify-between p-3 bg-secondary rounded-md">
                    <span className="font-mono">{project}</span>
                    <Button variant="outline" onClick={() => handleOpenProject(project)}>
                      Open
                    </Button>
                  </li>
                ))}
              </ul>
            ) : (
              <p className="text-muted-foreground text-center py-4">No projects found. Create one to get started!</p>
            )}
          </CardContent>
        </Card>
      </main>
    </div>
  );
}
```

---

<h2 id="packagesfrontendsrcpageseditorpagetsx"><code>packages/frontend/src/pages/EditorPage.tsx</code></h2>

```typescript
import { useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { useProjectStore } from '@/stores/useProjectStore';
import EditorLayout from '@/components/editor/EditorLayout';
import { socket } from '@/lib/socket';
import { useProcessingStore } from '@/stores/useProcessingStore';

export default function EditorPage() {
  const { projectName } = useParams<{ projectName: string }>();
  const setProjectName = useProjectStore((state) => state.setProjectName);
  const { setProgress, addLog, setError, setComplete } = useProcessingStore();

  useEffect(() => {
    if (projectName) {
      setProjectName(projectName);
    }
  
    // --- SOCKET.IO EVENT LISTENERS ---
    socket.connect();
    
    socket.on('processing-progress', ({ progress }) => setProgress(progress));
    socket.on('processing-log', ({ log }) => addLog(log));
    socket.on('processing-error', ({ message }) => setError(message));
    socket.on('processing-complete', ({ path }) => setComplete(path));

    // Cleanup on component unmount
    return () => {
      socket.off('processing-progress');
      socket.off('processing-log');
      socket.off('processing-error');
      socket.off('processing-complete');
      socket.disconnect();
    };
  }, [projectName, setProjectName, setProgress, addLog, setError, setComplete]);

  return <EditorLayout />;
}
```

---

<h2 id="packagesfrontendsrcstoresuseprocessingstorets"><code>packages/frontend/src/stores/useProcessingStore.ts</code></h2>

```typescript
import { create } from 'zustand';

interface ProcessingState {
  isProcessing: boolean;
  progress: number;
  logs: string[];
  error: string | null;
  outputFilePath: string | null;
  startProcessing: () => void;
  setProgress: (progress: number) => void;
  addLog: (log: string) => void;
  setError: (error: string) => void;
  setComplete: (path: string) => void;
  reset: () => void;
}

export const useProcessingStore = create<ProcessingState>((set) => ({
  isProcessing: false,
  progress: 0,
  logs: [],
  error: null,
  outputFilePath: null,
  startProcessing: () => set({ isProcessing: true, progress: 0, logs: [], error: null, outputFilePath: null }),
  setProgress: (progress) => set({ progress }),
  addLog: (log) => set((state) => ({ logs: [...state.logs.slice(-100), log] })), // Keep last 100 logs
  setError: (error) => set({ error, isProcessing: false }),
  setComplete: (path) => set({ outputFilePath: path, isProcessing: false, progress: 100 }),
  reset: () => set({ isProcessing: false, progress: 0, logs: [], error: null, outputFilePath: null }),
}));

```

---

<h2 id="packagesfrontendsrcstoresuseprojectstorets"><code>packages/frontend/src/stores/useProjectStore.ts</code></h2>

```typescript
import { create } from 'zustand';

interface ProjectState {
  projectName: string | null;
  setProjectName: (name: string) => void;
}

// This store holds the name of the currently active project.
export const useProjectStore = create<ProjectState>((set) => ({
  projectName: null,
  setProjectName: (name) => set({ projectName: name }),
}));

```

---

<h2 id="packagesfrontendsrcstoresusequeuestorets"><code>packages/frontend/src/stores/useQueueStore.ts</code></h2>

```typescript
import { create } from 'zustand';

// Defines the structure for a single video clip to be processed.
export interface Clip {
  id: string; // A unique ID for each clip
  sourceVideo: string;
  startTime: number;
  endTime: number;
  // We can add more properties like speed, filters, etc. later
}

interface QueueState {
  queue: Clip[];
  addClip: (clip: Clip) => void;
  removeClip: (id: string) => void;
  reorderQueue: (clips: Clip[]) => void;
}

// This store manages the array of clips in the trim queue.
export const useQueueStore = create<QueueState>((set) => ({
  queue: [],
  addClip: (clip) => set((state) => ({ queue: [...state.queue, clip] })),
  removeClip: (id) => set((state) => ({ queue: state.queue.filter((c) => c.id !== id) })),
  reorderQueue: (clips) => set({ queue: clips }),
}));

```

---

<h2 id="packagesfrontendsrcstoresusesettingsstorets"><code>packages/frontend/src/stores/useSettingsStore.ts</code></h2>

```typescript
import { create } from 'zustand';

// Defines the structure for global FFmpeg settings.
export interface FFmpegSettings {
  outputFormat: 'mp4' | 'mov' | 'gif';
  videoCodec: 'H.264 (libx264)' | 'H.265 (libx265)';
  audioCodec: 'AAC' | 'MP3';
  quality: number; // CRF value, e.g., 26
  encodingSpeed: 'ultrafast' | 'fast' | 'medium' | 'slow';
  combineClips: boolean;
}

interface SettingsState {
  settings: FFmpegSettings;
  setSettings: (newSettings: Partial<FFmpegSettings>) => void;
}

// This store holds all the global configuration options for video processing.
export const useSettingsStore = create<SettingsState>((set) => ({
  settings: {
    outputFormat: 'mp4',
    videoCodec: 'H.264 (libx264)',
    audioCodec: 'AAC',
    quality: 26,
    encodingSpeed: 'fast',
    combineClips: true,
  },
  setSettings: (newSettings) => set((state) => ({
    settings: { ...state.settings, ...newSettings },
  })),
}));

```

---

<h2 id="packagesfrontendsrcstoresusevideoplayerstorets"><code>packages/frontend/src/stores/useVideoPlayerStore.ts</code></h2>

```typescript
import { create } from 'zustand';

interface VideoPlayerState {
  // The source URL for the video player
  activeVideoSource: string | null;
  // Function to set the active video
  setActiveVideo: (source: string | null) => void;
}

// This store holds the state of the video player, primarily the source of the video to be played.
export const useVideoPlayerStore = create<VideoPlayerState>((set) => ({
  activeVideoSource: null,
  setActiveVideo: (source) => set({ activeVideoSource: source }),
}));
```

---

<h2 id="packagesfrontendsrcviteenvdts"><code>packages/frontend/src/vite-env.d.ts</code></h2>

```typescript
/// <reference types="vite/client" />

```

---

<h2 id="packagesfrontendtailwindconfigcjs"><code>packages/frontend/tailwind.config.cjs</code></h2>

```
/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ["class"],
  content: [
    './pages/**/*.{ts,tsx}',
    './components/**/*.{ts,tsx}',
    './app/**/*.{ts,tsx}',
    './src/**/*.{ts,tsx}',
  ],
  prefix: "",
  theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      keyframes: {
        "accordion-down": {
          from: { height: "0" },
          to: { height: "var(--radix-accordion-content-height)" },
        },
        "accordion-up": {
          from: { height: "var(--radix-accordion-content-height)" },
          to: { height: "0" },
        },
      },
      animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
}
```

---

<h2 id="packagesfrontendtailwindconfigjs"><code>packages/frontend/tailwind.config.js</code></h2>

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ["class"],
  content: [
    './pages/**/*.{ts,tsx}',
    './components/**/*.{ts,tsx}',
    './app/**/*.{ts,tsx}',
    './src/**/*.{ts,tsx}', // This line is crucial for scanning all files in src
  ],
  prefix: "",
  theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      colors: { // Using theme variables for consistency
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
      keyframes: {
        "accordion-down": {
          from: { height: "0" },
          to: { height: "var(--radix-accordion-content-height)" },
        },
        "accordion-up": {
          from: { height: "var(--radix-accordion-content-height)" },
          to: { height: "0" },
        },
      },
      animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
}
```

---

<h2 id="packagesfrontendtsconfigappjson"><code>packages/frontend/tsconfig.app.json</code></h2>

```json
{
  "compilerOptions": {
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.app.tsbuildinfo",
    "target": "ES2022",
    "useDefineForClassFields": true,
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "moduleDetection": "force",
    "noEmit": true,
    "jsx": "react-jsx",
    "baseUrl": ".",
    "paths": {
      "@/*": [
        "src/*"
      ]
    },

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "erasableSyntaxOnly": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true
  },
  "include": ["src"]
}

```

---

<h2 id="packagesfrontendtsconfigjson"><code>packages/frontend/tsconfig.json</code></h2>

```json
{
  "files": [],
  "references": [
    { "path": "./tsconfig.app.json" },
    { "path": "./tsconfig.node.json" }
  ],
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": [
        "src/*"
      ]
    }
  }
}

```

---

<h2 id="packagesfrontendtsconfignodejson"><code>packages/frontend/tsconfig.node.json</code></h2>

```json
{
  "compilerOptions": {
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.node.tsbuildinfo",
    "target": "ES2023",
    "lib": ["ES2023"],
    "module": "ESNext",
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "moduleDetection": "force",
    "noEmit": true,

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "erasableSyntaxOnly": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true
  },
  "include": ["vite.config.ts"]
}

```

---

<h2 id="packagesfrontendviteconfigts"><code>packages/frontend/vite.config.ts</code></h2>

```typescript
import path from "path"
import react from "@vitejs/plugin-react"
import { defineConfig } from "vite"

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  server: {
    // This proxy setting is crucial for development
    // It tells the Vite dev server to forward any requests to /api
    // to our backend server running on port 5001.
    proxy: {
      '/api': {
        target: 'http://localhost:5001',
        changeOrigin: true,
        secure: false,
      },
    },
  },
})
```

---

