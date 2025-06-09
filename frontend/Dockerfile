FROM node:18-alpine as builder
WORKDIR /app

# Copy package files
COPY package.json ./

# Install dependencies and generate lockfile
RUN npm install && \
    npm install react-scripts@5.0.1 -g && \
    [ -f package-lock.json ] || npm i --package-lock-only

# Copy app files
COPY public ./public
COPY src ./src

# Build
RUN npm run build

FROM nginx:1.23-alpine
COPY --from=builder /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]