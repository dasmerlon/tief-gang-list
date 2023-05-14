interface PageHeaderProps {
  readonly title: string;
}

export default function PageHeader(props: PageHeaderProps) {
  return (
    <h1 className="grow items-center px-8 p-4 mb-4 font-header text-2xl bg-slate-100 w-full">
      {props.title}
    </h1>
  );
}
