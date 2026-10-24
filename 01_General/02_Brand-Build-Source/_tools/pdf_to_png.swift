// swift pdf_to_png.swift <file.pdf> <outdir>  -> text.txt + p01.png... (xem lại PDF bằng ảnh; máy không có pdftoppm)
import PDFKit
import AppKit
let a = CommandLine.arguments
let doc = PDFDocument(url: URL(fileURLWithPath: a[1]))!
let out = a[2]
try? FileManager.default.createDirectory(atPath: out, withIntermediateDirectories: true)
var txt = ""
for i in 0..<doc.pageCount {
  let p = doc.page(at: i)!
  txt += "\n===== PAGE \(i+1) =====\n" + (p.string ?? "")
  let r = p.bounds(for: .mediaBox)
  let s: CGFloat = 1100 / max(r.width, r.height)
  let img = p.thumbnail(of: NSSize(width: r.width*s, height: r.height*s), for: .mediaBox)
  if let t = img.tiffRepresentation, let b = NSBitmapImageRep(data: t), let png = b.representation(using: .png, properties: [:]) {
    try? png.write(to: URL(fileURLWithPath: "\(out)/p\(String(format: "%02d", i+1)).png"))
  }
}
try? txt.write(toFile: "\(out)/text.txt", atomically: true, encoding: .utf8)
